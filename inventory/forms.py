from django import forms
from .models import *

class FoodForm(forms.ModelForm):
    class Meta:
        model = Foods
        fields = ('type', 'price', 'status', 'issues')


class DrinkForm(forms.ModelForm):
    class Meta:
        model = Drinks
        fields = ('type', 'price', 'status', 'issues')
        

class OtherForm(forms.ModelForm):
    class Meta:
        model = Others
        fields = ('type', 'price', 'status', 'issues')
