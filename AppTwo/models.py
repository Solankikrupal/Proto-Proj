from django.db import models


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length = 264)
    last_name = models.CharField(max_length = 264)
    e_mail = models.EmailField(max_length = 264)

    
