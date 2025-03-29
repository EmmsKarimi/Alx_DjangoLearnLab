from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from taggit.forms import TagWidget
from .models import Comment, Post

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class PostForm(forms.ModelForm):
    tags = forms.CharField(
        required=False,
        widget=TagWidget(attrs={'class': 'form-control', 'placeholder': 'Add tags separated by commas'})
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
