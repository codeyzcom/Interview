from rest_framework import serializers

from apps.userapp import models


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Profile
        fields = '__all__'

    level_name = serializers.ReadOnlyField(source='level.name')
