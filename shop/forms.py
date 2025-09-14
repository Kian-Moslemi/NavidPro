from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Product

class CustomSigninForm(UserCreationForm):
    address_title = forms.CharField(
        max_length=50,
        label='عنوان ادرس',
        widget=forms.TextInput(attrs={
            'class':'form-group',
            'placeholder':'خونه یا محل‌کار'
        }))
    address_line = forms.CharField(
        label='ادرس',
        widget = forms.TextInput(attrs={
            'class':'form-group',
            'placeholder':'ادرس....',
        }))
    password1 = forms.CharField(
        label='رمزعبور',
        widget=forms.PasswordInput,help_text=None
    )
    password2 = forms.CharField(
        label='تایید رمزعبور',
        widget=forms.PasswordInput,help_text=None
    )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({
            'class':'form-group',
            'placeholder':'test@gmail.com'
        })
        self.fields['first_name'].widget.attrs.update({
            'class':'form-group',
            'placeholder':'نام...'
        })
        self.fields['last_name'].widget.attrs.update({
            'class':'form-group',
            'placeholder':'نام خانوادگی'
        })        
        self.fields['username'].widget.attrs.update({
            'class':'form-group',
            'placeholder':'نام کاربری'
        })
        self.fields['password1'].widget.attrs.update({
            'class':'form-group',
            'placeholder':'رمزعبور'
        })
        self.fields['password2'].widget.attrs.update({
            'class':'form-group',
            'placeholder':'تایید رمزعبور'
        })
    class Meta:
        model = User
        fields = [
            'first_name','last_name','username','email','address_title',
            'address_line','password1','password2'
        ]
        labels = {
            'first_name':'نام',
            'last_name':'نام خانوادگی',
            'username':'نام کاربری',
            'email':'ایمیل',
        }
        help_texts = {
            'username':None,
        }
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['size']

