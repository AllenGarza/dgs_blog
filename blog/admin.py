from django.contrib import admin
from .models import Post

admin.site.register(Post) # make model visible on the admin page.