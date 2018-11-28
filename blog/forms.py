from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = {'title', 'story', 'cat_image', 'riddle', 'riddle_image', 'next_url', 'hint'}

class AnswerForm(forms.Form):
    answer = forms.CharField(max_length=50, min_length=1)