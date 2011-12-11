from django.contrib.sites.models import Site
from chapters.models import Chapter


class ChapterRoutingMiddleware(object):
    def process_request(self, request):
        domain_name = request.META.get('SERVER_NAME')
        if not domain_name:
            domain_name = Site.objects.get_current().domain
        parts = domain_name.split('.')
        subdomain = parts[0]
        try:
            chapter = Chapter.objects.get(subdomain=subdomain)
        except Chapter.DoesNotExist:
            chapter = None
        request.chapter = chapter
