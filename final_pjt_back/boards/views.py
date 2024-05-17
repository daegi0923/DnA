from django.shortcuts import render
from .models import Board, Comment
from .serializers import BoardSerializer, CommentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model
# Create your views here.


User = get_user_model()
@api_view(['POST'])
def create_board(request):
    if request.method == 'POST':
        serializer = BoardSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            print(request.user)
            serializer.save(user= request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)        


@api_view(['GET'])
def read_board_list(request):
    if request.method == 'GET':
        boards = Board.objects.all()
        serializer = BoardSerializer(boards, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

@api_view(['GET', 'DELETE', 'PUT'])
def read_board_detail(request, board_id):
    board = Board.objects.get(id=board_id)
    if request.method == 'GET':
        serializer = BoardSerializer(board)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        board.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = BoardSerializer(data=request.data, partial=True, instance=board)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
@api_view(['POST', 'GET'])
def read_board_comment(request, board_id):
    board = Board.objects.get(id=board_id)
    if request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            print(request.user)
            serializer.save(user = request.user, board=board)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == 'GET':
        comments = board.comment_set.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

@api_view(['DELETE'])
def delete_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    if request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)