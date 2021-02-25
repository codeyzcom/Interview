from rest_framework import viewsets

from apps.dictionary import (
    models,
    serializers,
)


class PositionViewAPI(viewsets.ModelViewSet):
    queryset = models.Position.objects.all()
    serializer_class = serializers.PositionSerializer


class LevelViewAPI(viewsets.ModelViewSet):
    queryset = models.Level.objects.all()
    serializer_class = serializers.LevelSerializer


class LanguageViewAPI(viewsets.ModelViewSet):
    queryset = models.Language.objects.all()
    serializer_class = serializers.LanguageSerializer


class FrameworkViewAPI(viewsets.ModelViewSet):
    queryset = models.Framework.objects.all()
    serializer_class = serializers.FrameworkSerializer
