from django import forms
from .models import Leaf


class FormName(forms.Form):

    sepal_length = forms.IntegerField()
    sepal_width  = forms.IntegerField()  
    petal_length = forms.IntegerField()
    petal_width  = forms.IntegerField()   
    predictions  = forms.CharField(max_length=256)

class FormNamedata(forms.ModelForm):
    class Meta:
        model = Leaf
        fields = ['sepal_length','sepal_width','petal_length','petal_width','predictions']    