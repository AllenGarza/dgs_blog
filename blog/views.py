from django.shortcuts import render
# Views take a web request and creates a web response. response can be HTML, XML, 404, etc.


def post_list(request):
    return render(request, 'blog/post_list.html', {})
