from django.contrib import admin
from .models import LoginForm,SignupForm

# Register your models here.


admin.site.register(LoginForm)
admin.site.register(SignupForm)