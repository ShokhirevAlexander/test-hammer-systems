from django import forms
from .models import CustomeUser


class CodeForm(forms.ModelForm):
    password_phone = forms.CharField(label='Введите пароль', widget=forms.TextInput(
        attrs={'placeholder': 'Введите пароль'}
    ))

    class Meta:
        model = CustomeUser
        fields = ('password_phone',)
