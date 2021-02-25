from django_filters import rest_framework as filters

from apps.userapp import models


class ProfileFilter(filters.FilterSet):
    class Meta:
        model = models.Profile
        fields = ('position', 'level')
