from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django.forms import ModelForm
class UserForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username","email","password1","password2"]
    def __init__(self,*args,**kwargs):
        super(UserForm,self).__init__(*args,**kwargs)
        for name,field in self.fields.items():
            field.widget.attrs.update({"class":"form-control"})

class UserProfile(ModelForm):
    class Meta:
        model=UserProfile
        fields=["profilName","profilImage"]
        def __init__(self,*args,**kwargs):
            super(UserProfile,self).__init__(*args,**kwargs)
            for name,field in self.fields.items():
                field.widget.attrs.update({"class":"form-control"})
        


