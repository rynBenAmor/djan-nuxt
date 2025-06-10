from django.contrib import admin

# Register your models here.
from .models import Message, Post

admin.site.register([Message,Post])