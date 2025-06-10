from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    quantity = models.PositiveIntegerField()
    created_at = models.DateField(auto_now_add=False, blank=True, null=True)

    def __str__(self):
        return str(self.title)
    