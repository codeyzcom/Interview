from rest_framework import viewsets

from apps.kernel import (
    models,
    serializers,
)


class InterviewTaskViewAPI(viewsets.ModelViewSet):
    queryset = models.InterviewTask.objects.all()
    serializer_class = serializers.InterviewTaskSerializer


class InterviewQuestionViewAPI(viewsets.ModelViewSet):
    queryset = models.InterviewQuestion.objects.all()
    serializer_class = serializers.InterviewQuestionSerializer


class InterviewViewAPI(viewsets.ModelViewSet):
    queryset = models.Interview.objects.all()
    serializer_class = serializers.InterviewSerializer


class InterviewTaskToInterviewViewAPI(viewsets.ModelViewSet):
    queryset = models.InterviewTaskToInterview.objects.all()
    serializer_class = serializers.InterviewTaskToInterviewSerializer


class InterviewQuestionToInterviewViewAPI(viewsets.ModelViewSet):
    queryset = models.InterviewQuestionToInterview.objects.all()
    serializer_class = serializers.InterviewQuestionToInterviewSerializer
