from django import forms
from .validators import russian_email
from django.core.validators import MinLengthValidator

from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.forms import TextInput, EmailInput, FileInput, Select


class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User

        fields = ['username', 'email', 'first_name', 'last_name']
        widgets = {'username': TextInput({'class': 'textinput form-control newinput',
                                          'placeholder': 'username',
                                          'id':'inputformcolor'}),
                   'email': EmailInput({'class': 'textinput form-control',
                                        'placeholder': 'email'}),
                   'first_name': TextInput({'class': 'textinput form-control',
                                            'placeholder': 'First name'}),
                   'last_name': TextInput({'class': 'textinput form-control',
                                           'placeholder': 'Last name'}),
                   }

#https://stackoverflow.com/questions/72278524/in-django-forms-i-cant-use-regex-validators
#https://stackoverflow.com/questions/29865320/django-form-field-regex-validation-for-alphanumeric-characters
from .models import Account
from django.core.validators import RegexValidator
class AccountUpdateForm(forms.ModelForm):

    class Meta:
        model = Account
        fields = ['phone', 'address','vk','instagram','telegram', 'account_image']
        widgets = {'phone': TextInput(attrs={'class': 'textinput form-control',
                                       "type":"tel",
                                       "placeholder": '+7(___)___-__-__',
                                       "required":"required",
                                       },
                                      ),
                   'address': TextInput({'class': 'textinput form-control',
                                         'placeholder': 'address'}),
                   'vk': TextInput({'class': 'textinput form-control',
                                      'placeholder': 'vk'}),
                   'instagram': TextInput({'class': 'textinput form-control',
                                         'placeholder': 'instagram'}),
                   'telegram': TextInput({'class': 'textinput form-control',
                                           'placeholder': 'telegram'}),
                   'account_image': FileInput({'class': 'form-control',
                                       'placeholder': 'image'})
                   }

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100,
                           validators = [MinLengthValidator(2)],
                           initial='Имя')
    email = forms.EmailField(validators=[russian_email])
    message = forms.CharField(widget=forms.TextInput, disabled=False)
    demo = forms.BooleanField(required = False, help_text='Текст-подсказка',
                              label='Вам нравится?',
                              initial=True)

