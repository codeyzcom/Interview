from django.urls import path, include

from rest_framework.routers import DefaultRouter

from apps.kernel import views

router = DefaultRouter()
router.register('interview', views.InterviewViewAPI)
router.register('interview_task', views.InterviewTaskViewAPI)
router.register('interview_question', views.InterviewQuestionViewAPI)
router.register(
    'interview_task_to_interview', views.InterviewTaskToInterviewViewAPI
)
router.register(
    'interview_question_to_interview', views.InterviewQuestionToInterviewViewAPI
)

app_name = 'kernel'
urlpatterns = [
    path('', include(router.urls)),

]
