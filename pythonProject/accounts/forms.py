from django import forms
from .models import CustomeUser
from referral.models import ReferralUser


class UserRegisterForm(forms.ModelForm):
    phone_number = forms.CharField(label='Номер телефона', widget=forms.TextInput(
        attrs={'class': 'form-label',
               'placeholder': 'введите номер телефона'}))

    class Meta:
        model = CustomeUser
        fields = ('phone_number',)


class UserProfileForm(forms.ModelForm):
    invite_code = forms.CharField(
        max_length=6,
        widget=forms.TextInput(attrs={'placeholder': 'Введите код приглашения'})  # noqa
    )

    class Meta:
        model = ReferralUser
        fields = ('he_invited_me',)
