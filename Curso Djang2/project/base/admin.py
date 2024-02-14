from django.contrib import admin
from .models import User, Comment

# Register your models here.

from .models import Post
admin.site.register(Post)
admin.site.register(Comment)