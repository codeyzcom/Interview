from django.contrib import admin

from apps.kernel import models


class InterviewQuestionToInterviewInline(admin.TabularInline):
    model = models.InterviewQuestionToInterview
    extra = 0


class InterviewTaskToInterviewInline(admin.StackedInline):
    model = models.InterviewTaskToInterview
    extra = 0


@admin.register(models.InterviewTask)
class InterviewTaskAdmin(admin.ModelAdmin):
    pass


@admin.register(models.InterviewQuestion)
class InterviewQuestionAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Interview)
class InterviewAdmin(admin.ModelAdmin):
    inlines = [
        InterviewQuestionToInterviewInline,
        InterviewTaskToInterviewInline
    ]


@admin.register(models.InterviewTaskToInterview)
class InterviewTaskToInterviewAdmin(admin.ModelAdmin):
    pass


@admin.register(models.InterviewQuestionToInterview)
class InterviewQuestionToInterviewAdmin(admin.ModelAdmin):
    pass
