from django.urls import path, include

from rest_framework.routers import DefaultRouter

from apps.dictionary import views

router = DefaultRouter()
# router.register('weapon', views)

app_name = 'dictionary'
urlpatterns = [
    path('', include(router.urls)),

]
