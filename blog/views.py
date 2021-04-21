from django.shortcuts import render
from .models import Post
from django.utils import timezone
# Views take a web request and creates a web response. response can be HTML, XML, 404, etc.


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
