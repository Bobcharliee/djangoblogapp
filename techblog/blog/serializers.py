
from rest_framework import serializers
from .models import blog

class blogserializer(serializers.ModelSerializer):
  class Meta:
    model= blog
    fields= ('author', 'title', 'description')