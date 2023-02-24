from django.forms import ModelForm, TextInput
from polls.models import *
from django import forms




class ModelesFormClass(ModelForm):
    class Meta:
        model = History
        fields = ['amount','adress']

        widgets = {
            "amount" : TextInput(attrs={
                'class': 'form-control form-control-static',
                'placeholder': 'Сумма'
            }),
            "adress" : TextInput(attrs={
                'class': 'form-control form-control-static',
                'placeholder': 'Адрес получателя'
            })
        }
