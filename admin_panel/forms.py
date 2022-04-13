from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _

from admin_panel.models import Outlet, Product


class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Enter Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.CharField(label='Enter Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {'email': 'Email'}
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'})
        }


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'class': 'form-control', 'autofocus': True}))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class': 'form-control'}),
    )


class OutletForm(forms.ModelForm):
    class Meta:
        model = Outlet
        fields = ['name', 'address', 'phone', 'manager_name', 'address_latitude', 'address_longitude', 'opening_time', 'closing_time', 'off_day','outlet_image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control'}),
            'manager_name': forms.TextInput(attrs={'class': 'form-control'}),
            'address_latitude': forms.NumberInput(attrs={'class': 'form-control'}),
            'address_longitude': forms.NumberInput(attrs={'class': 'form-control'}),
            'opening_time': forms.TimeInput(format='%H:%M:%S', attrs={'class': 'form-control'}),
            'closing_time': forms.TimeInput(format='%H:%M:%S', attrs={'class': 'form-control'}),
            'off_day': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ProductForm(forms.ModelForm):
    class Meta:
        CATEGORY_CHOICES = (
            ('S', 'Shirts'),
            ('P', 'Pants'),
            ('W', 'Watch'),
            ('T', 'Tie'),
            ('SH', 'Shoes'),
        )
        model = Product
        fields = ['title', 'selling_price', 'discount_price', 'descriptions', 'brand', 'category', 'product_image']
        # fields = "__all__"
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'selling_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'discount_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'descriptions': forms.TextInput(attrs={'class': 'form-control'}),
            'brand': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=CATEGORY_CHOICES, attrs={'class': 'form-control'}),
            # 'product_image': forms.ImageField(attrs={'class': 'form-control'}),
        }
