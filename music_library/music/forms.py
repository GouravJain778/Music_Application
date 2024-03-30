# forms.py
from django import forms
from .models import Folder, User
from django.contrib.auth.forms import UserCreationForm
from .models import Folder, Music
from django.core.validators import FileExtensionValidator

  # Adjust fields according to your Folder model

class MusicForm(forms.ModelForm):
    file_upload = forms.FileField(
        validators=[FileExtensionValidator(allowed_extensions=['mp3', 'wav', 'ogg'])]
    )

    class Meta:
        model = Music
        fields = ['title', 'artist', 'genre', 'file_upload']



class FolderForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = ['name']  # Add more fields as needed


class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
