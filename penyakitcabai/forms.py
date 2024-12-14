from django import forms

class UploadFileFrom(forms.Form):  
    image = forms.FileField()
