from django.db import models

# Create your models here.

class ChatMessage(models.Model):
    sender = models.CharField(max_length=100, default='user')  # Set default value to 'user'
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)