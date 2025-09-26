from rest_framework.exceptions import ValidationError
from rest_framework import serializers

from event.models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'title', 'description' , 'date' , 'location' , 'creator' , 'invited_user']



class EventCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'title', 'description' , 'date' , 'location' , 'creator' , 'invited_user']
        extra_kwargs = {
            'creator': {'required': False},
            'invited_user' : {'required' : False}
        }

    def create(self, validated_data):
        current_user = self.context.get("current_user")
        invited_users = validated_data.get('invited_user')

        event  = Event.objects.create(
            title=validated_data.get("title"),
            date=validated_data.get("date"),
            description=validated_data.get("description"),
            location=validated_data.get("location"),
            creator=current_user,
        )
        event.save()

        if not invited_users:
            event.invited_user.add(current_user)
        else:
            event.invited_user.add(current_user , *invited_users)

        return event


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



class EventRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['invited_user']

    def update(self, instance, validated_data):
        current_user = self.context.get('current_user')
        invited_user = instance.invited_user
        if invited_user.filter(id=current_user.id).exists():
                raise ValidationError("you alraedy registered in this event")
        invited_user.add(current_user)
        return instance


