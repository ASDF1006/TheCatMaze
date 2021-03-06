from django.shortcuts import render, render_to_response
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.template import RequestContext
from django.utils import timezone
from .models import Post
from .forms import PostForm
from .forms import AnswerForm

def main(request):
    posts = Post.objects.all()
    return render(request, 'blog/main.html', {'posts' : posts})

def riddle(request, answer):
    post = get_object_or_404(Post, post_url=answer)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if(form.is_valid()):
            return redirect(riddle, answer=request.POST.get('answer'))
    else:
        form = AnswerForm()
    return render(request, 'blog/riddle.html', {'post' : post, 'form' : form})

#404 page
'''
def page_not_found(request):
    response = render_to_response('blog\\404.html', {},
                context_instance=RequestContext(request))
    response.status_code = 404
    return response
'''

# 회원가입
def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(main)
    else:
        form = UserCreationForm
    return render(request, 'registration/signup.html', {'form':form})

# 문제 추가
@login_required
def riddle_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        dbProg = Progress.objects.get(title="dbProgress")
        if form.is_valid():
            newPost = form.save(commit=False)
            newPost.author = request.user
            newPost.published_date = timezone.now()
            newPost.postProgress = dbProg.dbProgress
            Post.PriorPostSet(newPost, dbProg) 
            dbProg.ProgressUp() 
            newPost.save()
            return redirect(riddle, answer=newPost.post_url)
    else:
        form = PostForm()

    return render(request, 'blog/riddle_new.html', {'form':form})

'''
@login_required
def riddle_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.progress = Post.Progress
            Post.PostSet(post)
            post.save()
            return redirect(riddle, answer=post.post_url)
    else:
        form = PostForm()
    return render(request, 'blog\\riddle_new.html', {'form':form})
'''
