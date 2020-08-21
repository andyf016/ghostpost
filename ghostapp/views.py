from django.shortcuts import render, HttpResponseRedirect, reverse
from ghostapp.models import Post
from ghostapp.forms import PostForm

def index(request):
    all_posts = Post.objects.all().order_by('-time_stamp')
    return render(request, 'index.html', {"posts": all_posts})

def post_form_view(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Post.objects.create(
                boast=data.get('sentiment'),
                post_content=data.get('post_content'),
                up_votes=0,
                down_votes=0,
            )
        return HttpResponseRedirect(reverse('home'))
    form = PostForm()

    return render(request, 'generic_form.html', {'form': form})

def upvote_view(request, post_id):
    current_post = Post.objects.get(id=post_id)
    current_post.total_votes += 1
    current_post.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def downvote_view(request, post_id):
    current_post = Post.objects.get(id=post_id)
    current_post.total_votes -= 1
    current_post.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def boast_view(request):
    boasts = Post.objects.filter(boast=True).order_by('-time_stamp')
    return render(request, 'index.html', {"posts": boasts})

def roast_view(request):
    roasts = Post.objects.filter(boast=False).order_by('-time_stamp')
    return render(request, 'index.html', {"posts": roasts})

def sorted_view(request):
    all_posts = Post.objects.all().order_by('-total_votes')
    return render(request, 'index.html', {"posts": all_posts})