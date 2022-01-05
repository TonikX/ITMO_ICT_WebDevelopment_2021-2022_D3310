from django import forms
from .models import Comment
from django.contrib.auth.models import User


class CommentForm(forms.ModelForm):
    text_comment = forms.CharField(label="Comment", required=False)
    point = forms.CharField(label="Point")
    b_date = forms.DateField(label="Begin time", required=False)
    e_date = forms.DateField(label="End time", required=False)

    class Meta:
        model = Comment
        fields = [
            "text_comment",
            "point",
            "b_date",
            "e_date"
        ]
        widgets = {
            "b_date": forms.DateInput(attrs={'type': 'date'}),
            "e_date": forms.DateInput(attrs={'type': 'date'})
        }


class UserForm(forms.ModelForm):
    username = forms.CharField(label="username")
    password = forms.CharField(widget=forms.PasswordInput(), label="password")
    email = forms.CharField(label="Email address")
    first_name = forms.CharField(label="first_name")
    last_name = forms.CharField(label="last_name")

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')

