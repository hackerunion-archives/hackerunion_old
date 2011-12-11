from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render
from annoying.decorators import render_to
from django.core.validators import email_re

@render_to('people/profile.html')
def profile(request, username):
    user = get_object_or_404(User, username=username)
    # `user` variable is already taken by a context processor
    return {'hacker': user}

# Do the signup.
# - Validate the fields and redirect them back to the form
# - Or, Create the user, log them in, and send them to dashboard
def signup(request):
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
    if User.objects.filter(username=email).exists():
        errors.append('The email is already taken.')

    # Re-render the form with validation errors, if necessary.
    if errors:
        return render(request, 'people/signup.html', {'errors': errors})

    # Success!  Create the user.
    user = User.objects.create_user(email, password)
    # TODO: Log them in
    return render(request, 'people/signup_confirmation.html', {'hacker': user})

