from django.urls import path, include

from rest_framework.routers import DefaultRouter

from apps.dictionary import views

router = DefaultRouter()
router.register('position', views.PositionViewAPI)
router.register('level', views.LevelViewAPI)
router.register('language', views.LanguageViewAPI)
router.register('framework', views.FrameworkViewAPI)


app_name = 'dictionary'
urlpatterns = [
    path('', include(router.urls)),

]
