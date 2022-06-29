from distutils.command.upload import upload
from pyexpat import model
from secrets import choice
from tkinter import CASCADE
from typing import Type
import uuid
from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files import File
from embed_video.fields import EmbedVideoField



    
class User(models.Model):
    TypeUserOpt = [
('NORMAL',"Normal"),
('EDITOR',"Editor"),
]   

    username = models.CharField(primary_key=True, max_length=50, null = False)
    password = models.CharField(max_length=50, null = False)
    TypeUser = models.CharField(max_length = 10, null=False, choices = TypeUserOpt)
    
    def __str__(self):
        return self.username



class Album(models.Model):
    id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User,related_name='User_albuns',on_delete = models.CASCADE)
    title_Album = models.CharField(max_length=50, null = False)
    cover_path = models.ImageField(upload_to = "Imagens/Capas_Albuns")
    description = models.CharField(max_length=50, null=False)
        
    def __str__(self):
        return self.title_Album
    
    class Meta:
        ordering = ['title_Album']
    

class Music(models.Model):
    id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
    title_Music = models.CharField(max_length=50, null = False)
    create_at = models.DateTimeField(auto_now_add=True)
    music_path = models.FileField(upload_to="Music/%y")
    length = models.PositiveIntegerField(default=1)
    album = models.ForeignKey(Album,related_name="Album_Tracks",on_delete = models.CASCADE)
    def __str__(self):
        return self.title_Music
    
    class Meta:
        ordering = ['-create_at']
    

class Artist(models.Model):
    id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, null = False)
    photo_path = models.ImageField(upload_to = "Imagens/Artistas")
    description = models.CharField(max_length=50, null=True)
    music = models.ForeignKey(Music,on_delete = models.CASCADE)
    def __str__(self):
        return self.name
    

class Critics(models.Model):
    choice = [
("Pessimo",'0'),
("Mau",'1'),
("Agradavel",'2'),
("Bom",'3'),
("Muito Bom", '4'),
("Excelente", '5'),
]    
    id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
    album = models.ForeignKey(Album,related_name='Album_critic',on_delete = models.CASCADE)
    score = models.CharField(max_length=10,choices=choice)
    description = models.CharField(max_length=50)
    
    class Meta:
        ordering = ['-album']
        
    def __str__(self):
        return self.album
    
    

class Video(models.Model):
    id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50, null = False)
    create_at = models.DateTimeField(auto_now_add=True)
    path = models.FileField(upload_to="Videos/%y")
    length = models.PositiveIntegerField(null = False)
    description = models.CharField(max_length=50, null = True)
    urlStreaming = EmbedVideoField(null = True) 
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    def __str__(self):
        return self.title
    
    
    class Meta:
        ordering = ['-create_at']
        
        
class shareGroup(models.Model):
    id  = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, null = False)
    description = models.CharField(max_length=50, null = True)
    music = models.ForeignKey(Music,default = "",on_delete = models.CASCADE)
    video = models.ForeignKey(Video,default = "",on_delete = models.CASCADE)
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    
    def __str__(self):
        return self.name

class GroupAdm(models.Model):
   GroupFK =  models.ForeignKey(shareGroup,on_delete = models.CASCADE)
   UserFK = models.ForeignKey(User,on_delete = models.CASCADE)


