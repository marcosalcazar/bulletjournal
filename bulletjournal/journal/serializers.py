from rest_framework import serializers
from journal.models import Task, Event, Note

#WORKAROUND as in https://code.djangoproject.com/ticket/10405#comment:11
from django.db.models.loading import cache as model_cache
if not model_cache.loaded:
    model_cache.get_models()


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note


class DaySerializer(serializers.Serializer):
    day = serializers.DateTimeField()
    tasks = TaskSerializer(many=True)
    events = EventSerializer(many=True)
    notes = NoteSerializer(many=True)

    @property
    def id(self):
        return unicode(self.day)