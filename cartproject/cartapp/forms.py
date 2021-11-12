from django import forms
from django.contrib.auth.forms import UserCreationForm #Django already has built in forms for user auth
from django.contrib.auth.models import User


# Crete your forms here

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True) # the custom field we want

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=True)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
