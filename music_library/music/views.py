from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Music, Folder
from .forms import FolderForm, MusicForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import FolderForm, MusicForm, SignUpForm




def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('homepage')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('folderpage')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


@login_required
def user_logout(request):
    logout(request)
    return redirect('homepage')


@login_required
def create_folder(request):
    print(request.user.username)
    if request.method == 'POST':
        form = FolderForm(request.POST)
        if form.is_valid():
            new_folder = form.save(commit=False)
            print(new_folder)
            new_folder.owner_id = request.user.id
            new_folder.save()
            return redirect('folderpage')  # Redirect to homepage or any other desired page
    else:
        form = FolderForm()
    return render(request, 'registration/create_folder.html', {'form': form})


@login_required
def add_to_folder(request, folder_id):
    folder = get_object_or_404(Folder, id=folder_id)
    all_music_tracks = Music.objects.all()
    if request.method == 'POST':
        music_id = request.POST.get('music_id')
        music = get_object_or_404(Music, id=music_id)
        folder.music_tracks.add(music)
        return redirect('folderpage')  # Redirect to folder detail page
    else:
            return render(request, 'registration/select_music.html', {'folder': folder, 'all_music_tracks': all_music_tracks})
        # Render a form to select the music track
    


@login_required
def folder_detail(request, folder_id):
    folder = get_object_or_404(Folder, id=folder_id)
    return render(request, 'registration/folder_detail.html', {'folder': folder})


@login_required
def delete_folder(request, folder_id):
    folder = get_object_or_404(Folder, id=folder_id)
    if request.method == 'POST':
        folder.delete()
        return redirect('folderpage')  # Redirect to homepage or any other desired page
    return render(request, 'registration/confirm_delete_folder.html', {'folder': folder})


@login_required
def update_folder(request, folder_id):
    folder = get_object_or_404(Folder, id=folder_id)
    if request.method == 'POST':
        form = FolderForm(request.POST, instance=folder)
        if form.is_valid():
            form.save()
            return redirect('folderpage')  # Redirect to folder detail page
    else:
        form = FolderForm(instance=folder)
    return render(request, 'registration/update_folder.html', {'form': form, 'folder': folder})

def folderpage(request):
    folder= Folder.objects.all()
    return render(request, 'registration/folder.html',{'folder':folder})

def music_page(request):
    # Retrieve music tracks related to the specified folder
    music_tracks = Music.objects.all()
    return render(request, 'registration/music_page.html', {'music_tracks':music_tracks})

@login_required
def create_music(request):
    if request.method == 'POST':
        form = MusicForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('musicpage')  # Redirect to homepage or any other desired page
    else:
        form = MusicForm()
    return render(request, 'registration/create_music.html', {'form': form})


@login_required
def delete_music(request, music_id):
    music = get_object_or_404(Music, id=music_id)
    if request.method == 'POST':
        music.delete()
        return redirect('musicpage')  # Redirect to homepage or any other desired page
    return render(request, 'registration/confirm_delete_music.html', {'music': music})


@login_required
def update_music(request, music_id):
    music = get_object_or_404(Music, id=music_id)
    if request.method == 'POST':
        form = MusicForm(request.POST, instance=music)
        if form.is_valid():
            form.save()
            return redirect('musicpage')  # Redirect to homepage or any other desired page
    else:
        form = MusicForm(instance=music)
    return render(request, 'registration/update_music.html', {'form': form, 'music': music})


def homepage(request):
    music_tracks = Music.objects.all()
    return render(request, 'registration/homepage.html', {'music_tracks': music_tracks})
