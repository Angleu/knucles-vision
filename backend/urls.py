from django.contrib import admin
from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
  
   path('Users', views.Users, name="Users"),  
   path('Streaming/Videos', views.StreamVideos),     
   path('Streaming/Musicas', views.StreamMusic),     
   path('Register', views.Register, name="Register"),  
   path('User/<str:pk>', views.DetailsUser, name="DetailsUser"),
   path('User/<str:pk>/UpdateUserInfo', views.UpdateUserInfo, name="UpdateUser"),
   path('User/<str:pk>/DeleteAccount', views.DeleteUserAccount, name="DeleteUserAccount"),
   path('User/<str:pk>/CreateAlbum', views.CreateAlbum),
   path('User/<str:pk>/UpdateAlbum', views.UpdateAlbumInfo),
   path('User/<str:pk>/DeleteAlbum', views.DeleteAlbum),
   path('User/<str:pk>/CreateArtist', views.CreateArtist),   
   path('User/<str:pk>/DeleteArtist', views.DeleteArtist),
   path('User/<str:pk>/CreateCritic', views.CreateCritc),  
   path('User/<str:pk>/DeleteCritic', views.DeleteCritic),
   path('User/<str:pk>/CreateGroup', views.CreateGroup),
   path('User/<str:pk>/UpdateMyGroup', views.UpdateGroupInfo),
   path('User/<str:pk>/DeleteGroup', views.DeleteGroup),
   path('User/<str:pk>/CreateVideo', views.CreateVideo),
   path('User/<str:pk>/DeleteVideo', views.DeleteVideo),  
   path('User/<str:pk>/CreateMusic', views.CreateMusic),
   path('User/<str:pk>/DeleteMusic', views.DeleteMusic),
   path('User/<str:pk>/UpdateMusicInfo', views.UpdateMusic),
  
 ]

#Create function for video url
if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)