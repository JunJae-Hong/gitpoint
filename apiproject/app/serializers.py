from app.models import Admin
from rest_framework import serializers

class AdminSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Admin
        fields = ('title', 'text')