import os

from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from event.models import Event
from event.serializers import EventSerializer, EventEditSerializer, EventCreateSerializer, EventRegisterSerializer
from rest_framework import status



class EventListCreateView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @extend_schema(
        request=EventSerializer,
        responses={200: EventSerializer(many=True) },
    )
    def get(self, request):
        title = request.query_params.get("title")
        description = request.query_params.get("description")
        date = request.query_params.get("date")
        location = request.query_params.get("location")

        event_list = Event.objects.all()

        if title:
            event_list = event_list.filter(title__icontains=title)
        if description:
            event_list = event_list.filter(description__icontains=description)
        if date:
            event_list = event_list.filter(date__icontains=date)
        if location:
            event_list = event_list.filter(location__icontains=location)

        serializer = EventSerializer(event_list, many=True)
        return Response(serializer.data)

    @extend_schema(
        request=EventCreateSerializer,
        responses={201: EventCreateSerializer},
    )
    def post(self, request):
        serializer = EventCreateSerializer(data=request.data ,  context={'current_user': request.user})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data , status=status.HTTP_200_OK)


class EventUpdateDeleteView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @extend_schema(
        request=EventEditSerializer,
        responses={200: EventEditSerializer},
    )
    def put(self, request, id):
        event = get_object_or_404(Event, id=id)
        serializer = EventEditSerializer(event , data=request.data , partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data , status=status.HTTP_200_OK)


class EventRegisterManager(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @extend_schema(
        request=None,
        responses={200: EventRegisterSerializer},
    )
    def put(self , request , id):
        event = get_object_or_404(Event , id=id)
        serializer = EventRegisterSerializer( event ,  data=request.data , partial=True , context={"current_user" : request.user })
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data , status=status.HTTP_200_OK)
