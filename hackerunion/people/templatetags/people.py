import hashlib
from django import template

register = template.Library()


@register.filter
def gravatar_url(user):
    cleaned_email = user.get_profile().contact_email.strip().lower()
    email_hash = hashlib.md5(cleaned_email).hexdigest()
    return "http://www.gravatar.com/avatar/%s?d=mm" % email_hash


def retrieve_first_service(user, name):
    svcs = user.services.filter(type__name=name)
    if not svcs.count():
        return None
    return svcs[0]


@register.filter
def facebook(user):
    return retrieve_first_service(user, 'Facebook')


@register.filter
def twitter(user):
    return retrieve_first_service(user, 'Twitter')


@register.filter
def tumblr(user):
    return retrieve_first_service(user, 'Tumblr')


@register.filter
def service_url(service):
    return service.type.username_url % service.username


@register.filter
def service_label(service):
    # XXX Special case Twitter here. We'll probably
    # eventually have to do this for more services,
    # so this really should be a field on the
    # ServiceType model, like `username_url`.
    if service.type.name == 'Twitter':
        return "@%s" % service.username
    proto_idx = service.type.username_url.index('://')
    label = service.type.username_url[proto_idx+3:]
    return label % service.username
