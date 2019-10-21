from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpadteForm
from logapp.models import Profile

def home(request):
    context = {
        'profile':Profile.objects.all()
    }
    return render(request,'logapp/home.html',context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('logapp:login')
    else:
        form = UserRegisterForm()
    return render(request, 'logapp/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpadteForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile
                                   )
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated !')
            return redirect('logapp:profile')
    else:
        u_form = UserUpdateForm()
        p_form = ProfileUpadteForm()

    context = {
        'u_form':u_form,
        'p_form':p_form

    }

    return render(request, 'logapp/profile.html', context)