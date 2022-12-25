from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Post

# Create your views here.
def home(request):
    context = {
        'posts': Post.objects.all(),
    }
    print('posts', Post.objects.all())
    return render(request, 'index.html', context)

def form(request):
    if request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']

        post = Post.objects.create(title=title, body=body)
        post.save()
        messages.info(request, 'Post created successfully')
        return redirect('/')

    return render(request, 'form.html')

def post(request, pk):
    found_post = Post.objects.get(pk=pk)
    context = {
        'post': found_post,
    }
    return render(request, 'post.html', context)
