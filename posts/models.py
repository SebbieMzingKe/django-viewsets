from pickle import TRUE
from django.db import models
from accounts.models import User
from django.contrib.auth import get_user_model
from django.conf import settings



# Create your models here.
# User = get_user_model
class Post(models.Model):
    title = models.CharField(max_length = 50)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,null=True,blank=True, on_delete=models.CASCADE, related_name = "posts")


    def __str__(self):
        return self.title
    