from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import CustomUser
from .serializers import UserSerializer


@api_view(["POST"])
def register(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
        )

    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST,
    )


@api_view(["POST"])
def login(request):
    return Response()


@api_view(["POST"])
def logout(request):
    return Response()


@api_view(["POST"])
def change_password(request):
    return Response()


@api_view(["POST"])
def delete_account(request):
    return Response()


@api_view(["GET"])
def get_user_data(request):
    return Response()
