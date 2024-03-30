from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass
    class Meta:
        # Add this inner class to prevent related_name clashes
        unique_together = ('email',)

    # Custom related_names to prevent clashes with auth app
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='music_user_groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='music_user_permissions',
        blank=True,
        help_text='Specific permissions for this user.'
    )



class Music(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    file_upload = models.FileField(upload_to='music/')


    def __str__(self):
        return self.title

class Folder(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    music_tracks = models.ManyToManyField(Music, related_name='folders')

    def __str__(self):
        return self.name


