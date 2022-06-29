import string

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.core.paginator import Paginator
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser


from .models import *
from .serializers import *


##############################UTILIZADOR
@api_view(['GET'])
def Users(request):
  serializer = UserSerializer(User.objects.all(),many =True)
  print(serializer.data)
  return JsonResponse({"Users": serializer.data}, safe = False)


#INSERIR NA BD(JSON)
@api_view(['POST'])
def Register(request):
  serializer = UserSerializer(data = request.data)
  if serializer.is_valid():
    serializer.save()
  return Response(serializer.data, status = status.HTTP_201_CREATED)


#DETALHES DE UM INDIVIDUO
@api_view(['GET'])
def DetailsUser(request, pk):
      albuns = AlbumSerializer(Album.objects.filter(user = pk), many = True)
      videos = VideoSerializer(Video.objects.filter(user = pk), many = True)     
      GroupsAdmin = GroupsAdmSerializer(GroupAdm.objects.filter(UserFK = pk), many = True) 
      Groups = GroupsSerializer(shareGroup.objects.filter(user = pk), many = True)
      return Response({"Albuns":albuns.data ,"Videos":videos.data ,"GroupsAdmin":GroupsAdmin.data, 'Groups':Groups.data})
    
    
#ACTUALIZAR INFORMACAO DO UTILIZADOR    
@api_view(['POST']) 
def UpdateUserInfo(request, pk):
      user = User.objects.get(username = pk)
      serializer = UserSerializer(user, data = request.data)
      if serializer.is_valid():
        serializer.save()
      return Response(serializer.data, status = status.HTTP_201_CREATED)

#ELIMINAR CONTA DE UTILIZADOR    
@api_view(['DELETE']) 
def DeleteUserAccount(request, pk):
      user = User.objects.get(username = pk)
      user.delete()
      return Response("USER DELETED")


################################################ALBUM
#INSERIR ALBUM NA BD(JSON)
@api_view(['POST'])
def CreateAlbum(request):
  serializer = AlbumSerializer(data = request.data)
  if serializer.is_valid():
    serializer.save()
  return Response(serializer.data, status = status.HTTP_201_CREATED)


 
#ACTUALIZAR INFORMACAO DO ALBUM    
@api_view(['POST']) 
def UpdateAlbumInfo(request, pk):
      Album = Album.objects.get(user = pk)
      serializer = AlbumSerializer(Album, data = request.data)
      if serializer.is_valid():
        serializer.save()
      return Response(serializer.data, status = status.HTTP_201_CREATED)

@api_view(['DELETE']) 
def DeleteAlbum(request, pk):
  if Album.objects.filter(user = pk):
    album = Album.objects.get(user = pk)
    album.delete()
    return Response("Album DELETED")
  
  


#################################################ARTIST
#INSERIR ARTISTA NA BD(JSON)
@api_view(['POST'])
def CreateArtist(request):
  serializer = ArtistSerializer(data = request.data)
  if serializer.is_valid():
    serializer.save()
  return Response(serializer.data, status = status.HTTP_201_CREATED) 



@api_view(['DELETE']) 
def DeleteArtist(request, pk): 
  if Artist.objects.filter(music = Music.objects.get(album = Album.objects.filter(user = pk))):
    Artist.objects.filter(music = Music.objects.get(album = Album.objects.filter(user = pk))).delete()
    return Response("Artist DELETED")
  
  
  
################################################VIDEO
#INSERIR VIDEO NA BD(JSON)
@api_view(['POST'])
def CreateVideo(request):
  serializer = VideoSerializer(data = request.data)
  if serializer.is_valid():
    serializer.save()
  return Response(serializer.data, status = status.HTTP_201_CREATED) 


@api_view(['DELETE']) 
def DeleteVideo(request, pk):
  if Video.objects.filter(user = pk):
    Video.objects.filter( user = pk).delete()
    return Response("Critic DELETED")
  
@api_view(['GET'])
def StreamVideos(request):
  serializer = VideoSerializer(Video.objects.all(),many =True)
  print(serializer.data)
  return JsonResponse({"Videos": serializer.data}, safe = False)
 
  
#INSERIR CRITICA NA BD(JSON)
@api_view(['POST'])
def CreateCritc(request):
  serializer = CriticSerializer(data = request.data)
  if serializer.is_valid():
    serializer.save()
  return Response(serializer.data, status = status.HTTP_201_CREATED) 
 

@api_view(['DELETE']) 
def DeleteCritic(request, pk):
  if Critics.objects.filter(album = Album.objects.get(user = pk)):
    Critics.objects.filter( album = Album.objects.get(user = pk)).delete()
    return Response("Critic DELETED")
  
  
#INSERIR NA BD(JSON)
@api_view(['POST'])
def CreateMusic(request):
  serializer = MusicSerializer(data = request.data)
  if serializer.is_valid():
    serializer.save()
  return Response(serializer.data, status = status.HTTP_201_CREATED)





def StreamMusic(request):
  serializer = MusicSerializer(Music.objects.all(),many =True)
  print(serializer.data)
  return JsonResponse({"Music": serializer.data}, safe = False)

  

@api_view(['DELETE']) 
def DeleteMusic(request, pk):  
  if Music.objects.filter( album = Album.objects.get(user = pk)):
    Music.objects.filter( album = Album.objects.get(user = pk)).delete()
    return Response("Music DELETED") 
 

@api_view(['POST']) 
def UpdateMusic(request, pk):
      Music = Music.objects.get(album = Album.objects.filter(user = pk))
      serializer = GroupsAdmSerializer(Music, data = request.data)
      if serializer.is_valid():
        serializer.save()
      return Response(serializer.data, status = status.HTTP_201_CREATED)
 

@api_view(['GET'])
def StreamMusic(request):
  serializer = MusicSerializer(Music.objects.all(),many =True)
  print(serializer.data)
  return JsonResponse({"Music": serializer.data}, safe = False)
 
@api_view(['POST'])
def CreateGroup(request):
  serializer = GroupsSerializer(data = request.data)
  if serializer.is_valid():
    serializer.save()
  return Response(serializer.data, status = status.HTTP_201_CREATED)

@api_view(['POST']) 
def UpdateGroupInfo(request, pk):
      MyGroup = GroupAdm.objects.get(UserFK = pk)
      serializer = GroupsAdmSerializer(MyGroup, data = request.data)
      if serializer.is_valid():
        serializer.save()
      return Response(serializer.data, status = status.HTTP_201_CREATED)

 
@api_view(['DELETE']) 
def DeleteGroup(request, pk):
  if shareGroup.objects.filter(Users = pk):
    shareGroup.objects.filter(Users = pk).delete()
    return Response("GROUP DELETED")
  
  
def stream(request):
  paginator = Paginator(Music.objects.all(), 1)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)
  return render (request, 'Stream.html', {"Music":page_obj})
