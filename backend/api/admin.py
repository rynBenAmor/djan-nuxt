from django.contrib import admin

# Register your models here.
from .models import Message, Comment, Profile

admin.site.register([Message, Comment, Profile])