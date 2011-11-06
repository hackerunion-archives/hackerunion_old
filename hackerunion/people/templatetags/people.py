import hashlib
from django import template

register = template.Library()


@register.filter
def gravatar_url(user):
    if not user.email:
        return None
    cleaned_email = user.email.strip().lower()
    email_hash = hashlib.md5(cleaned_email).hexdigest()
    return "http://www.gravatar.com/avatar/%s?d=mm" % email_hash
