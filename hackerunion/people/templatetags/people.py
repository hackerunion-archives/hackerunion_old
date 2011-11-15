import hashlib
from django import template
from hackerunion.people.models import AVAILABILITY_CHOICES

register = template.Library()


@register.filter
def gravatar_url(user):
    cleaned_email = user.get_profile().contact_email.strip().lower()
    email_hash = hashlib.md5(cleaned_email).hexdigest()
    return "http://www.gravatar.com/avatar/%s?d=mm" % email_hash


@register.filter
def availability(availability_code):
    for code, string in AVAILABILITY_CHOICES:
        if code == availability_code:
            return string
    return ''
