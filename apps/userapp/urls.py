from django.urls import path, include

from rest_framework.routers import DefaultRouter

from apps.userapp import views

router = DefaultRouter()
# router.register('weapon', views)

app_name = 'userapp'
urlpatterns = [
    path('', include(router.urls)),

]
