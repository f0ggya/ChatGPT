from django.db import models
from django.contrib.auth.models import User

class Chat(models.Model):
    name = models.TextField('chat_name')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

class Message(models.Model):
    text = models.TextField('text')
    from_who = models.IntegerField('from_who')
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)

class Setting(models.Model):
    theme = models.CharField('theme', choices=[
        ('light_theme', 'light theme'),
        ('dark_theme', 'dark theme')
    ], max_length=255
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=1)



