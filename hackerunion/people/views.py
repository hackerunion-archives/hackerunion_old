from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from annoying.decorators import render_to


@render_to('people/profile.html')
def profile(request, username):
    user = get_object_or_404(User, username=username)
    # `user` variable is already taken by a context processor
    return {'hacker': user}
