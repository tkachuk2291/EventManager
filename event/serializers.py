from rest_framework import serializers

from event.models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'title', 'description' , 'date' , 'location']

class EventEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'title', 'description' , 'date' , 'location']
        extra_kwargs = {
            'title': {'required': False},
            'description': {'required': False},
            'date': {'required': False},
            'location': {'required': False},
        }