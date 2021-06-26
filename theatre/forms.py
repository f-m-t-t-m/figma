from theatre.models import *
from django.forms import ModelForm, TextInput, Textarea
from django import forms


class MaecenasForm(ModelForm):
    class Meta:
        model = Maecenas
        fields = '__all__'

        widgets = {
            "name": TextInput(attrs={
                "class": 'text-form',
                "placeholder": 'Имя',
            }),
            "phone": TextInput(attrs={
                "class": 'text-form',
                "placeholder": 'Телефон',
            }),
            "company": TextInput(attrs={
                "class": 'text-form',
                "placeholder": 'Компания',
            }),
            "mail": TextInput(attrs={
                "class": 'text-form',
                "placeholder": 'E-mail',
            }),
            "message": Textarea(attrs={
                "class": 'grid-ta',
                "placeholder": 'Сообщение'
            }),
        }