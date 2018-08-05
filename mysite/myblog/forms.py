from django.forms import ModelForm
From myblog.models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'author', 'category']
