from django.contrib import admin
from .models import Post,Message

# Register your models here.
admin.site.register(Post)
admin.site.register(Message)

# admin.site.register(comments)
# admin.site.register(Rating)
