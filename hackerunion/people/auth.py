import logging
from django.contrib.auth.models import User, check_password

logger = logging.getLogger(__name__)


class EmailBackend(object):
    def authenticate(self, username=None, password=None):
        try:
            user = User.objects.get(email=username)
        except User.DoesNotExist:
            logger.warning('No user for %s', username)
        except User.MultipleObjectsReturned:
            logger.error('Multiple users for email %s', username)
        else:
            if check_password(password, user.password):
                return user
        return None
    
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
