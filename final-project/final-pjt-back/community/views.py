from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.contrib.auth.decorators import login_required
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import Community, Comment
from .serializers import CommunitySerializer, CommentSerializer

# Create your views here.
@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def community_list_create(request):
    if request.method == 'GET':
        community_lists = Community.objects.all()
        serializer = CommunitySerializer(community_lists, many=True)
        return Response(serializer.data)
    else:
        serializer = CommunitySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

# get보다 먼저 나와야 함
@api_view(['PUT', 'DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def community_detail(request, community_pk):
    community = get_object_or_404(Community, pk=community_pk)

    if request.method == 'DELETE':
        community.delete()
        response = {'pk': community_pk}
        return Response(response, status=status.HTTP_204_NO_CONTENT)
    else : 
        # PUT
        serializer = CommunitySerializer(community, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def community_detail(request, community_pk):
        community = get_object_or_404(Community, pk=community_pk)
        serializer = CommunitySerializer(community)
        return Response(serializer.data)
        

@api_view(['GET', 'POST'])
def comments(request, community_pk):
    community = get_object_or_404(Community, pk=community_pk)
    if request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(community=community)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        comment_list = get_list_or_404(Comment, community=community)
        serializer = CommentSerializer(comment_list, many=True)
        return Response(serializer.data)


@api_view(['PUT', 'DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def comment_detail(request, community_pk, comment_pk):
    community = get_object_or_404(Community, pk=community_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'DELETE':
        comment.delete()
        response = {'pk': comment_pk}
        return Response(response, status=status.HTTP_204_NO_CONTENT)
    else:
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)