from django import forms
 
# import GeeksModel from models.py
from .models import ChatRoom
 
# create a ModelForm
class CreateForm(forms.ModelForm):
    
    class Meta:
        model = ChatRoom
        fields = ['name','slug']