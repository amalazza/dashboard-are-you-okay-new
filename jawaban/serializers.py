from .models import Jawaban
from rest_framework import serializers

class CreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jawaban
        fields = ('jawaban')