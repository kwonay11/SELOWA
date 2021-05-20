from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render, get_list_or_404
from .models import Community, Comment
from .serializers import CommunitySerializer, CommentSerializer

# Create your views here.


def community_list(request):
    community_lists = Community.objects.all()
    serializer = CommunitySerializer(community_lists, many=True)
    return Response(serializer.data)

