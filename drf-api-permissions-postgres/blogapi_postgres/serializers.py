from rest_framework import serializers
from .models import blogapi_postgres

class blogapi_postgresSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'owner', 'title', 'specification', 'created_at')
        model = blogapi_postgres