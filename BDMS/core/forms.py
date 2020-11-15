from django import forms
from .models import donarmodel,contactmodel

"""class donarform(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(donarform,self).__init__(*args,**kwargs)
        self.label_suffix=' '
    class Meta:
        model=donarmodel
        fields="__all__"
        labels={
            'name':'Full Name','phone':'Mobile Number','email':'Email Address','age':'Age',
            'gender':'Select Gender','bgroup':'Select Blood Group','address':'Address'
        }
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'phone':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'age':forms.TextInput(attrs={'class':'form-control'}),
            'gender':forms.Select(attrs={'class':'form-control'}),
            'bgroup':forms.Select(attrs={'class':'form-control'}),
            'address':forms.Textarea(attrs={'class':'form-control','rows':3})
        }"""


    
