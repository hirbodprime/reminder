from rest_framework import serializers as s
from .models import AlarmModel

class AlarmModelSerializer(s.ModelSerializer):
    class Meta:
        model = AlarmModel
        # fields = '__all__'
        exclude = ['TimesUp']