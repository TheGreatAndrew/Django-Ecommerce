from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Driver


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)

class DriverForm(forms.ModelForm):

    class meta:
        model = Driver

        fields = [

            "order",
            "is_available",

        ]