from django.shortcuts import render
from ghostapp.models import Post

def index(request):
    all_posts = Post.objects.all()
    return render(request, 'index.html', {"posts": all_posts})
