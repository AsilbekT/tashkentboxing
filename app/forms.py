from django import forms
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox
  
  
class ContactForm(forms.Form):
    name = forms.CharField()
    surname = forms.CharField()
    number = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)

    name.widget.attrs.update({'class': 'contact__input', "placeholder": "Name"})
    surname.widget.attrs.update({'class': 'contact__input', "placeholder": "surname"})
    number.widget.attrs.update({'class': 'contact__input', "placeholder": "number"})
    email.widget.attrs.update({'class': 'contact__input', "placeholder": "email"})
    message.widget.attrs.update({'class': 'contact__input', "placeholder": "Your messages"})