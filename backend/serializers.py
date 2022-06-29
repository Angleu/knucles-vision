from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        

class GroupsAdmSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupAdm
        fields = '__all__'
        
class GroupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = shareGroup
        fields = '__all__'     
           
class CriticSerializer(serializers.ModelSerializer):
    class Meta:
        model = Critics
        fields = '__all__'


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'
        


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'
      
class MusicSerializer(serializers.ModelSerializer):
      class Meta:
        model = Music
        fields = '__all__'
       

        
class AlbumSerializer(serializers.ModelSerializer):
    Album_Tracks = MusicSerializer(many=True, read_only=True)    
    Album_Artist = ArtistSerializer(many = True, read_only = True)
    Album_critic = CriticSerializer(many=True, read_only=True)
    class Meta:
        model = Album
        fields = '__all__'

