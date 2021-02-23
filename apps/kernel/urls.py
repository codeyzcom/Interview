from django.urls import path, include

from rest_framework.routers import DefaultRouter

from apps.kernel import views

router = DefaultRouter()
# router.register('weapon', views)

app_name = 'kernel'
urlpatterns = [
    path('', include(router.urls)),

]
