from django.shortcuts import render, redirect
from .forms import UserInfoCreationForm, UserInfoChangeForm, ProfileForm
from django.contrib.auth.forms import PasswordChangeForm
from homesapp.forms import AgentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserInfoCreationForm(request.POST)
        if form.is_valid():
            user_type = form.cleaned_data.get('is_agent')
            form_obj = form.save(commit=False)
            form_obj.is_agent = user_type
            form_obj.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! Please login to continue.')
            return redirect('login')
    else:
        form = UserInfoCreationForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def userprofile(request):
    args = {'user': request.user}
    if request.user.is_agent:
        return render(request, 'homesapp/agent_profile.html', args)
    else:
        return render(request, 'users/userprofile.html', args)

@login_required
def editprofile(request):
    if request.method == 'POST':
        u_form = UserInfoChangeForm(request.POST, instance=request.user)
        if request.user.is_agent:
            p_form = AgentForm(request.POST,
                                       request.FILES,
                                       instance=request.user.agent)
        else:
            p_form = ProfileForm(request.POST, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('myprofile')

    else:
        u_form = UserInfoChangeForm(instance=request.user)
        if request.user.is_agent:
            p_form = AgentForm(instance=request.user.agent)
        else:
            p_form = ProfileForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/edit_user.html', context)

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, request.user)
            messages.success(request, 'Your password has been changed!')
            return redirect('myprofile')

    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'users/change_password.html', {'form': form})