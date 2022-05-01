from django.shortcuts import render
from requests import request
from myapp.models import Profile, Item
from myapp.forms import ProfileForm
from django.shortcuts import get_object_or_404, redirect
from myapp.forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout #add this
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import ListView
import json 
from django.http import HttpResponse
import datetime


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

# def login_request(request):
# 	if request.method == "POST":
# 		form = AuthenticationForm(request, data=request.POST)
# 		if form.is_valid():
# 			username = form.cleaned_data.get('username')
# 			password = form.cleaned_data.get('password')
# 			user = authenticate(username=username, password=password)
# 			if user is not None:
# 				login(request, user)
# 				messages.info(request, f"You are now logged in as {username}.")
# 				return redirect("home")
# 			else:
# 				messages.error(request,"Invalid username or password.")
# 		else:
# 			messages.error(request,"Invalid username or password.")
# 	form = AuthenticationForm()
# 	return render(request=request, template_name="login.html", context={"login_form":form})

def google(request):
    message="id:%s, uasername:%s firstname:%s, lastname:%s"%(request.user.pk, request.username, request.user.first_name, request.user.last_name)
    now = datetime.datetime.now()
    template_name="login.html"
    return HttpResponse(template_name)





def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.") 
    return HttpResponse()

data =[] 

class ItemListView(ListView):
    model = Item
    paginate_by = 3
    #queryset=Bike.objects.filter(type='mountain')
    template_name = 'item_list.html'


def add_to_cart(request):
    global data
    pk = request.POST.get("pk", "")
    title = request.POST.get("title", "")
    myitem={
        "pk": pk,
        "tile": title,
        "quantity": 1
        }
    data += [myitem,]
    dictionary = {"data": data}
    json_object = json.dumps(dictionary, indent = 4)
    print(json_object)
    response = redirect('home')
    response.set_cookie('cart', json_object)
    return response


from django.http import HttpResponse
from PIL import Image
import libscrc
import qrcode


def calculate_crc(code):
    crc = libscrc.ccitt_false(str.encode(code))
    crc = str(hex(crc))
    crc = crc[2:].upper()
    return crc.rjust(4, '0')

def gen_code(mobile="", nid="", amount=1.23):
    code="00020101021153037645802TH29370016A000000677010111"
    if mobile:
        tag,value = 1,"0066"+mobile[1:]
        seller='{:02d}{:02d}{}'.format(tag,len(value), value)
    elif nid:
        tag,value = 2,nid
        seller='{:02d}{:02d}{}'.format(tag,len(value), value)
    else:
        raise Exception("Error: gen_code() does not get seller mandatory details")
    code+=seller
    tag,value = 54, '{:.2f}'.format(amount)
    code+='{:02d}{:02d}{}'.format(tag,len(value), value)
    code+='6304'
    code+=calculate_crc(code)
    return code

def get_qr(request,mobile="",nid="",amount=""):
    message="mobile: %s, nid: %s, amount: %s"%(mobile,nid,amount)
    print( message )
    code=gen_code(mobile=mobile, amount=float(amount))#scb
    print(code)
    img = qrcode.make(code,box_size=4)
    response = HttpResponse(content_type='image/png')
    img.save(response, "PNG")
    return response

def checkout(request):
    context={
        "mobile":"0826639206", #seller's mobile
        "amount": 2.81619
    }
    return render(request, 'checkout.html', context)


