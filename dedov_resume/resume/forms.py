from django import forms
from captcha.fields import CaptchaField

class SendMailForm(forms.Form):
    name = forms.CharField(max_length=255, label='Ваше имя')
    email = forms.EmailField(max_length=255, label='Ваш E-mail')
    content = forms.CharField(label='Ваше сообщение', widget=forms.Textarea(attrs={'cols':60, 'rows':10}))
    captcha = CaptchaField(label='Введите код ')