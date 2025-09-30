<<<<<<< HEAD
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# ฟอร์มสมัครสมาชิก
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

# ฟอร์มล็อกอิน
class LoginForm(forms.Form):
    username = forms.CharField()
=======
# uiuser/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=15, required=False)
    address = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'phone', 'address', 'password1', 'password2', 'role')

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus': True}))
>>>>>>> 2b6a10c (ทำหน้เา html ทั้งหมด)
    password = forms.CharField(widget=forms.PasswordInput)
