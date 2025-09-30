from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

User = get_user_model()   # ✅ ใช้ฟังก์ชันนี้แทนการ import User ตรง ๆ

# ฟอร์มสมัครสมาชิก
class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

# ฟอร์มล็อกอิน
class LoginForm(AuthenticationForm):   # ✅ ให้สืบทอดจาก AuthenticationForm ไปเลย
    pass
