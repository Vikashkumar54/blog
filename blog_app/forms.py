from django import forms
from .models import add,contactu,proimage


class addform(forms.ModelForm):
    class Meta:
        model=add
        fields='__all__'

class contactform(forms.ModelForm):
    class Meta:
        model=contactu
        fields='__all__'
        
class proimageform(forms.ModelForm):
    class Meta:
        model=proimage
        fields='__all__'
        
