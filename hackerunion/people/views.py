from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render, \
                             render_to_response
from django.core.validators import email_re
from people.models import HackerProfile


def people_list(request):
    profs = HackerProfile.objects.filter(chapter=request.chapter)
    users = User.objects.filter(pk__in=profs.values_list('user__pk', flat=True))
    return render(request, 'people/list.html', {'hackers': users})


def userid(request, userid):
    user = get_object_or_404(User, pk=userid)
    if user.username != user.email:
        # The user has set a custom username, so redirect
        # to the "friendly" URL
        return redirect(user.get_profile())
    return render(request, 'people/profile.html', {'hacker': user})


def profile(request, username):
    user = get_object_or_404(User, username=username)
    # `user` variable is already taken by a context processor
    return render(request, 'people/profile.html', {'hacker': user})


def signup(request):
    """Do the signup.
    - Validate the fields and redirect them back to the form
    - Or, Create the user, log them in, and send them to dashboard
    """
    if request.method == 'GET':
        return render(request, 'people/signup.html')

    # Get the parameters
    email = request.REQUEST['email']
    password = request.REQUEST['password']
    password2 = request.REQUEST['password2']

    # Validate
    errors = []
    if password != password2:
        errors.append('The passwords do not match')
    if len(password) < 6:
        errors.append('Password must be at least 6 characters.')
    if not email_re.match(email):
        errors.append('Email is not valid.')
    email_filter = Q(username=email) | Q(email=email)
    if User.objects.filter(email_filter).exists():
        errors.append('The email is already taken.')

    # Re-render the form with validation errors, if necessary.
    if errors:
        return render(request, 'people/signup.html', {'errors': errors})

    # Success!  Create the user.
    user = User.objects.create_user(email, email, password=password)
    assert request.chapter is not None, \
           'user hit a signup page outside of chapter'
    prof = HackerProfile.objects.create(user=user, chapter=request.chapter)

    # TODO: Log them in
    return render(request, 'people/signup_confirmation.html', {'hacker': user})


def list(request):
    'Show a list of all users in the chapter.'
    hackers = HackerProfile.objects.all() # filter(chapter=request.chapter)
    return render(request, 'people/list.html', {'hackers': hackers})
