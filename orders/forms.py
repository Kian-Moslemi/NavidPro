from django import forms
from .models import Address,Order


class OrderForm(forms.ModelForm):
    address  = forms.ModelChoiceField(
        queryset=Address.objects.none(),
        empty_label='انتخاب ادرس',
        label='ادرس'
    )
    class Meta:
        required_css_class = 'required'
        model = Order
        fields = ['first_name','last_name','phone','address','postal_code','email']
        widgets = {
            'first_name':forms.TextInput(attrs={
                'placeholder':'نام خود را وارد کنید'
            }),
            'last_name':forms.TextInput(attrs={
                'placeholder':'نام خانوادگی را وارد کنید'
            }),
            'phone':forms.TextInput(attrs={
                'placeholder':'شماره تماس را وارد کنید'
            }),
            'postal_code':forms.TextInput(attrs={
                'placeholder':'کد پستی خود را وارد  کنید'
            }),
            'email':forms.EmailInput(attrs={
                'placeholder':'ایمیل خود را وارد کنید'
            })
        }
        labels = {
            'first_name':'نام',
            'last_name':'نام خانوادگی',
            'phone':'شماره تماس',
            'address':'ادرس',
            'postal_code':'کد پستی',
            'email':'ایمیل',
        }

    def __init__(self,*args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        
        self.fields['address'].queryset = Address.objects.filter(user=user)
        
        choices = list(self.fields['address'].choices)
        choices.append(("add_new","+ افزودن ادرس جدید"))
        self.fields['address'].choices = choices

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['title','address_line']

        widgets = {
            'title':forms.TextInput(attrs={
                'placeholder':'خونه، محل کار.....'
            }),
        }