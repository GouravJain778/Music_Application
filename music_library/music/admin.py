from django.contrib import admin

# Register your models here.
from .models import User, Music, Folder

admin.site.register(User)
admin.site.register(Music)
admin.site.register(Folder)
