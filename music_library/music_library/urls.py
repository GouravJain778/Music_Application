"""
URL configuration for music_library project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from music import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='homepage'),
    path('create_folder/', views.create_folder, name='create_folder'),
    path('add_to_folder/<int:folder_id>/', views.add_to_folder, name='add_to_folder'),
    path('folder_detail/<int:folder_id>/', views.folder_detail, name='folder_detail'),
    path('delete_folder/<int:folder_id>/', views.delete_folder, name='delete_folder'),
    path('update_folder/<int:folder_id>/', views.update_folder, name='update_folder'),
    path('music/',views.music_page, name='musicpage'),
    path('folderpage/' , views.folderpage , name="folderpage"),
    path('create_music/', views.create_music, name='create_music'),
    path('delete_music/<int:music_id>/', views.delete_music, name='delete_music'),
    path('update_music/<int:music_id>/', views.update_music, name='update_music'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
  
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
