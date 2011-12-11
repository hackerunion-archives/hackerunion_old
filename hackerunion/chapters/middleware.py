import datetime
import logging
from django.conf import settings
from django.contrib.sites.models import Site
from chapters.models import Chapter

logger = logging.getLogger(__name__)


class ChapterRoutingMiddleware(object):
    def process_request(self, request):
        if settings.DEBUG:
            return self.DEBUG_process_request(request)
        domain_name = request.META.get('SERVER_NAME')
        if not domain_name:
            domain_name = Site.objects.get_current().domain
        parts = domain_name.split('.')
        subdomain = parts[0]
        chapter = None
        try:
            chapter = Chapter.objects.get(subdomain=subdomain)
        except Chapter.DoesNotExist:
            pass
        request.chapter = chapter
    
    def DEBUG_process_request(self, request):
        chapter = None
        if request.COOKIES.get('use_domain'):
            subdomain = request.COOKIES['use_domain']
            try:
                chapter = Chapter.objects.get(subdomain=subdomain)
            except Chapter.DoesNotExist:
                chapter = Chapter.objects.get_default_chapter(request)
                logger.debug('Defaulting to chapter: %s', chapter)
        else:
            chapter = Chapter.objects.get_default_chapter(request)
        assert chapter is not None, 'chapter should be set in DEBUG mode'
        request.chapter = chapter

    def process_response(self, request, response):
        if settings.DEBUG and request.GET.get('c'):
            subdomain = request.GET['c']
            if Chapter.objects.filter(subdomain=subdomain).exists():
                age = datetime.timedelta(days=356)
                response.set_cookie('use_domain', subdomain,
                                    max_age=age.total_seconds())
                logger.debug('Set chapter: %s', subdomain)
            else:
                logger.debug('Chapter %s does not exist', subdomain)
        return response
