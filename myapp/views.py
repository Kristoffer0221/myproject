from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegistrationForm, LoginForm, TaskForm
from django.contrib.auth.decorators import login_required
from .models import Task
  

# Register View
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, 'Account created successfully! You can now log in.')
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'authentication/register.html', {'form': form})


# Login View
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username'].lower()
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)

                if user.is_superuser:
                    messages.success(request, f'Welcome Admin {user.username}!')
                    return redirect('/admin')
                else:
                    return redirect('home')  
            else:
                messages.error(request, 'Invalid username or password.')
                return redirect('login')
        else:
            messages.error(request, 'Please correct the errors below.')
            return redirect('login')
    else:
        form = LoginForm()

    return render(request, 'authentication/login.html', {'form': form})

@login_required
def home(request):
    task = Task.objects.filter(user=request.user)
    return render(request, 'home.html', {'task':task})


# Logout View
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    
@login_required
def add_task(request):
    if request.method == 'POST': #IF method is POST
        form = TaskForm(request.POST) #Get form
        if form.is_valid(): #If the form is valid
            task = form.save(commit=False)# Do not save to database immediately
            task.user = request.user # Because you want to get the assigned user first
            form.save()#then save the form
            return redirect('home')
    
    else:
        form = TaskForm()
        
        return render (request, "add_task.html", {'form':form})
