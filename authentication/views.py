from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, ProfileForm
from .models import Request
from django.contrib.auth.models import User
from django.db import transaction

def register_and_request_access(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            with transaction.atomic():
                user = user_form.save(commit=False)
                user.set_password(user_form.cleaned_data['password'])
                user.save()
                # The profile is created by the signal.
                # We pass the instance to the form to update it.
                profile_form = ProfileForm(request.POST, request.FILES, instance=user.profile)
                if profile_form.is_valid():
                    profile_form.save()
                    Request.objects.create(user=user)
                    return redirect('registration_complete')
    else:
        user_form = UserRegistrationForm()
        profile_form = ProfileForm()
    return render(request, 'authentication/register.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

def registration_complete(request):
    return render(request, 'authentication/registration_complete.html')
