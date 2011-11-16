import hashlib
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
def gravatar_url(user_profile):
    cleaned_email = user_profile.contact_email.strip().lower()
    email_hash = hashlib.md5(cleaned_email).hexdigest()
    return "http://www.gravatar.com/avatar/%s?d=mm" % email_hash


@register.filter
@stringfilter
def pretty_url(url):
    proto_idx = url.find('://')
    if proto_idx != -1:
        url = url[proto_idx+3:]
    if url.endswith('/'):
        url = url[:-1]
    return url
