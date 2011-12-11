from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render, \
                             render_to_response
from django.core.validators import email_re
from people.models import HackerProfile

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
    email_filter = Q(username=email) | Q(email=email)
    if User.objects.filter(email_filter).exists():
        errors.append('The email is already taken.')
    if hasattr(request, 'chapter'):
        chapter = request.chapter
    else:
        if settings.DEBUG:
            chapter = Chapter.objects.all()[0]
        else:
            errors.append('You must select a chapter to join.')

    # Re-render the form with validation errors, if necessary.
    if errors:
        return render(request, 'people/signup.html', {'errors': errors})

    # Success!  Create the user.
    user = User.objects.create_user(email, email, password=password)
    prof = HackerProfile.objects.create(user=user, chapter=chapter)
    
    # TODO: Log them in
    return render(request, 'people/signup_confirmation.html', {'hacker': user})
