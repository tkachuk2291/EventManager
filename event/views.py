from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from event.models import Event
from event.serializers import EventSerializer, EventEditSerializer


class EventListCreateView(APIView):
    def get(self ,  request):
        event_list = Event.objects.all()
        serializer = EventSerializer(event_list , many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


class EventUpdateDeleteView(APIView):
    def put(self, request, id):
        event = get_object_or_404(Event, id=id)
        serializer = EventEditSerializer(event , data=request.data , partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, id):
        event = get_object_or_404(Event, id=id)
        event.delete()
        return Response(f"delete for {id} done")




