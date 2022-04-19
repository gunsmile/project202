from django.shortcuts import render
from requests import request
from myapp.models import Profile
from myapp.forms import ProfileForm
from django.shortcuts import get_object_or_404, redirect
from myapp.forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout #add this
from django.contrib.auth.forms import AuthenticationForm

def home(request):
    context={
        'user':request.user,
        'toker':'mysecret'
    }
    return render(request, 'home.html',context=context)

def profile(request): 
    instance = get_object_or_404(Profile, user=request.user)
    form = ProfileForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('home')
    else:
        context = {
            'form':form,
            'user':request.user
            }
        return render(request, 'profile.html', context) 

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if  form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("home")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("home")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})

def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.") 
    return redirect("login")