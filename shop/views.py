from django.shortcuts import render,get_object_or_404
from .models import Category,Product
from django.shortcuts import render,redirect
from .forms import CustomSigninForm,ProductForm
from orders.models import Address
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from cart.forms import CartAddProductForm

def home_page(request):
    return render(request,'home.html',{})

def about_us(request):
    return render(request,'aboutus.html',{})

def call_us(request):
    return render(request,'callus.html',{})


def sign_in(request):
    if request.method == "POST":
        form = CustomSigninForm(request.POST)
        if form.is_valid():
           user = form.save(commit=False)
           user.email = form.cleaned_data['email']
           user.save()

           user = Address.objects.create(
               user = user,
               title = form.cleaned_data['address_title'],
               address_line = form.cleaned_data['address_line'],
            )
           return redirect('login')
    else:
        form = CustomSigninForm()
    return render(request,'signin.html',{'form':form})

def log_in(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'User doesnt exist')
            return redirect('login')

    return render(request,'login.html',{})

def log_out(request):
    logout(request)
    return redirect('home')


def hotsandwich(request):
    products = Product.objects.filter(category=1)
    form = CartAddProductForm()
    form2 = ProductForm()   
    return render(request,'hotsandwich.html',{'products':products,'form':form,'form2':form2})

def coldsandwich(request):
    products = Product.objects.filter(category=3)
    form = CartAddProductForm()
    return render(request,'coldsandwich.html',{'products':products,'form':form})

def drinks(request):
    products = Product.objects.filter(category=2)
    form = CartAddProductForm()
    return render(request,'drinks.html',{'products':products,'form':form})
