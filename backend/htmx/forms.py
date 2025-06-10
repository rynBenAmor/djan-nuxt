from django import forms
from .models import Message, Post
from tinymce.widgets import TinyMCE


class MessageForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 20}))

    class Meta:
        model = Message
        fields = '__all__'

class PostForm(forms.ModelForm):    
    title = forms.CharField(max_length=50, required=True, widget= forms.TextInput(
        attrs={"class": "form-control w-50 border-dark"}
    ))

    class Meta:
        model = Post
        fields = ('title',)