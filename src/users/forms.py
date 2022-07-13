from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from users.models import MyUser, UserProfile


class MyUserForm(UserCreationForm):
    # (UserCreationForm.Meta)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({
            'type': 'email',
            'class': 'form-control',
            'placeholder': 'Email',
        })
        self.fields['password1'].widget.attrs.update({
            'type': 'password',
            'class': 'form-control',
            'placeholder': 'Password',
        })
        self.fields['password2'].widget.attrs.update({
            'type': 'password',
            'class': 'form-control',
            'placeholder': 'Confirm the password'
        })

    class Meta:
        model = MyUser
        fields = ('email',)


class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
