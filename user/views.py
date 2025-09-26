from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from user.models import User
from user.serializers import UserSerializers, UserUpdateSerializers



class UserListCreateView(APIView):
    authentication_classes = [JWTAuthentication]

    @extend_schema(
        request=UserSerializers,
        responses={200: UserSerializers(many=True)},
        methods=["GET"]
    )
    def get(self, request, pk):
        if pk:
            user = get_object_or_404( User, id=pk)
            serializer = UserSerializers(user)
            return Response(serializer.data , status=status.HTTP_200_OK)
        serializer = UserSerializers(User.object.all() , many=True)
        return Response(serializer.data)

    @extend_schema(
        request=UserSerializers,
        responses={200: UserSerializers(many=True)},
        methods=["POST"]
    )
    def post(self , request):
        serializer = UserSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.data)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

class UserUpdateDeleteView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @extend_schema(
        request=UserUpdateSerializers,
        responses={200: UserUpdateSerializers(many=True)},
    )
    def put(self, request, pk):
        user = get_object_or_404(User, id=pk)
        serializer = UserUpdateSerializers(user, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data , status=status.HTTP_200_OK)

    def delete(self, request, pk):
        user = get_object_or_404(User, id=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)