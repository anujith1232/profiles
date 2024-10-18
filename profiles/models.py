from django.db import models

# Create your models here.
class Profile(models.Model):
    username = models.CharField(max_length=200)
    bio = models.TextField(max_length=200)
    skills = models.CharField(max_length=200)
    contact_email = models.EmailField()
    image = models.ImageField(upload_to='profile_media/')

    def __str__(self):
        return '{}'.format(self.username)