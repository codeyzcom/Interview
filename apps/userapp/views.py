from rest_framework import viewsets

from django_filters import rest_framework as django_filters

from apps.userapp import (
    models,
    serializers,
    filters,
)


class ProfileViewAPI(viewsets.ModelViewSet):
    queryset = models.Profile.objects.all()
    serializer_class = serializers.ProfileSerializer
    filter_backends = [django_filters.DjangoFilterBackend]
    filter_class = filters.ProfileFilter
