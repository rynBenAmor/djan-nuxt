from django.db import models
from tinymce.models import HTMLField

class Message(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    content = HTMLField(blank=True, null=True)
    



from textblob import TextBlob  # AI Sentiment Analysis

class Comment(models.Model):
    text = models.TextField()
    sentiment = models.CharField(max_length=10, blank=True)  # "positive", "neutral", "negative"


    def save(self, *args, **kwargs):
        analysis = TextBlob(self.text).sentiment.polarity
        if analysis > 0:
            self.sentiment = "positive"
        elif analysis < 0:
            self.sentiment = "negative"
        else:
            self.sentiment = "neutral"
        super().save(*args, **kwargs)
    
    
    def __str__(self):
        return self.text




class Profile(models.Model):
    CITY_CHOICES = [
        ('Tunis', 'Tunis'),
        ('Paris', 'Paris'),
        ('New York', 'New York'),
        ('Tokyo', 'Tokyo'),
        ('Cairo', 'Cairo'),
    ]
    
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=50, choices=CITY_CHOICES)

    def __str__(self):
        return f"{self.name} from {self.city}"





class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    summary = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        # Auto-generate summary
        blob = TextBlob(self.content)
        self.summary = " ".join(blob.noun_phrases[:5])  # Extract key phrases
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
