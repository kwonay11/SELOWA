from rest_framework import serializers
from .models import Community, Comment

class CommunitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Community
        fields = ('id', 'title', 'content', 'created_at', 'updated_at')

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'content')
