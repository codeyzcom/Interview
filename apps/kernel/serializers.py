from rest_framework import serializers

from apps.kernel import models


class InterviewQuestionToInterviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.InterviewQuestionToInterview
        fields = '__all__'


class InterviewTaskToInterviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.InterviewTaskToInterview
        fields = '__all__'


class InterviewTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.InterviewTask
        fields = '__all__'

    language_name = serializers.ReadOnlyField(source='language__name')
    level_name = serializers.ReadOnlyField(source='level__name')


class InterviewQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.InterviewQuestion
        fields = '__all__'

    language_name = serializers.ReadOnlyField(source='language__name')
    level_name = serializers.ReadOnlyField(source='level__name')
    framework_name = serializers.ReadOnlyField(source='framework__name')


class InterviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Interview
        fields = '__all__'

    question = InterviewQuestionToInterviewSerializer(
        many=True, required=False, read_only=True
    )
    task = InterviewTaskToInterviewSerializer(
        many=True, required=False, read_only=True
    )
    user_name = serializers.ReadOnlyField(source='user__name')
    result_level_name = serializers.ReadOnlyField(source='result_level__name')
    target_level_name = serializers.ReadOnlyField(source='target_level__name')
