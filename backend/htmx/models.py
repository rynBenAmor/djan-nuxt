# tasks_htmx/models.py

from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(default="")
    completed = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True,)

    def __str__(self):
        return self.title



from tinymce.models import HTMLField

class Message(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    content = HTMLField()


class Post(models.Model):
    '''Model definition for Post.'''
    title = models.CharField(max_length=50)
    likes = models.PositiveIntegerField(default=0)

    class Meta:
        '''Meta definition for Post.'''

        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return str(self.title)



