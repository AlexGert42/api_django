from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import *

# class AddPostForm(forms.Form):
#     title = forms.CharField(max_length=150, label='Title', widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
#     slug = forms.SlugField(max_length=150, label='Slug', widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
#     content = forms.CharField(max_length=1000, widget=forms.Textarea(attrs={'class': 'form-control', 'cols': 60, 'rows': 20}), label='Text' )
#     is_published = forms.BooleanField(label='Public', required=False, initial=True, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
#     cat = forms.ModelChoiceField(queryset=Category.objects.all(), label='Cetegory', required=False, empty_label='Category not selected', widget=forms.Select(attrs={'class': 'form-control form-select form-control-lg'}))



class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'Category not selected'

    class Meta:
        model = Post
        fields = ['title', 'slug', 'content', 'photo', 'is_published', 'cat']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'cols': 60, 'rows': 20}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 100:
            raise ValidationError('length > 100 simbols ')

        return title



class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'imput_formuser'}))
    password1 = forms.CharField(label='Пароль1', widget=forms.TextInput(attrs={'class': 'imput_formuser'}))
    password2 = forms.CharField(label='Пароль2', widget=forms.TextInput(attrs={'class': 'imput_formuser'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'imput_formuser'}),
            'password1': forms.TextInput(attrs={'class': 'imput_formuser'}),
            'password2': forms.TextInput(attrs={'class': 'imput_formuser'})
        }
