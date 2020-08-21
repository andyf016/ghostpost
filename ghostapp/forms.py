from django import forms
from ghostapp.models import Post

class PostForm(forms.Form):
    BOOL_CHOICES = ((True, 'Boast'), (False, 'Roast'))
    post_content = forms.CharField(widget=forms.Textarea)
    sentiment = forms.ChoiceField(choices = BOOL_CHOICES)