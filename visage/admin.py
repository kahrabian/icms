from django.contrib import admin

from visage.models import ProjectContent, Project, ExamContent, Exam, ExcerciseContent, Excercise, \
    NotificationContent, Notification, ContentFile, ContentTag, File, Tag, Content, CourseTeachingAssistant, \
    CourseProject, CourseExam, CourseExercise, CourseNotification, CourseContent, Course

admin.site.register(ProjectContent)
admin.site.register(Project)
admin.site.register(ExamContent)
admin.site.register(Exam)
admin.site.register(ExcerciseContent)
admin.site.register(Excercise)
admin.site.register(NotificationContent)
admin.site.register(Notification)
admin.site.register(ContentFile)
admin.site.register(ContentTag)
admin.site.register(File)
admin.site.register(Tag)
admin.site.register(Content)
admin.site.register(CourseTeachingAssistant)
admin.site.register(CourseProject)
admin.site.register(CourseExam)
admin.site.register(CourseExercise)
admin.site.register(CourseNotification)
admin.site.register(CourseContent)
admin.site.register(Course)
