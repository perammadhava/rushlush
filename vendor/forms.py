from django import forms
from .models import Product,Customer




class CustomerRegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Customer  # Set the model to Vendor
        fields = ['username', 'email', 'password', 'confirm_password']

class CustomerLoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)       

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'image', 'category', 'price', 'quantity']
