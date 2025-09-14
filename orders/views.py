from django.shortcuts import render,redirect
from .forms import OrderForm,AddressForm
from .models import Address
from django.contrib.auth.decorators import login_required

def order_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    if request.method == "POST":
        
        form = OrderForm(request.POST,user=request.user)
        if form.is_valid():
            order =  form.save(commit=False)
            order.user = request.user
            order.save()
    else:
        form = OrderForm(user=request.user)
    return render(request,'order.html',{'form':form})



@login_required
def add_address(request):
    if request.method == "POST":
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()
            return redirect('order')
    else:
        form = AddressForm()
    return render(request,'add_address.html',{'form':form})
