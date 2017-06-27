from django.db import models
from django.utils.translation import ugettext as _
from django.utils import timezone


class ProjectContent(models.Model):
    project = models.ForeignKey('Project', verbose_name=_('project'))
    content = models.ForeignKey('Content', verbose_name=_('content'))


class UserProject(models.Model):
    user = models.ForeignKey('authentication.User', verbose_name=_('user'))
    project = models.ForeignKey('Project', verbose_name=_('project'))
    score = models.PositiveIntegerField(verbose_name=_('score'), default=0, null=False)


class Project(models.Model):
    title = models.CharField(max_length=50, verbose_name=_('title'), null=False)
    score = models.PositiveIntegerField(verbose_name=_('score'), default=0, null=False)
    deadline = models.DateTimeField(verbose_name=_('deadline'), null=False)
    description = models.CharField(max_length=1000, verbose_name=_('description'), default='', null=True)
    contents = models.ManyToManyField('Content', verbose_name=_('contents'), through=ProjectContent)


class ExamContent(models.Model):
    exam = models.ForeignKey('Exam', verbose_name=_('exam'))
    content = models.ForeignKey('Content', verbose_name=_('content'))


class UserExam(models.Model):
    user = models.ForeignKey('authentication.User', verbose_name=_('user'))
    exam = models.ForeignKey('Exam', verbose_name=_('exam'))
    score = models.PositiveIntegerField(verbose_name=_('score'), default=0, null=False)


class Exam(models.Model):
    title = models.CharField(max_length=50, verbose_name=_('title'), null=False)
    score = models.PositiveIntegerField(verbose_name=_('score'), default=0, null=False)
    date = models.DateTimeField(verbose_name=_('date'), null=False)
    description = models.CharField(max_length=1000, verbose_name=_('description'), default='', null=True)
    contents = models.ManyToManyField('Content', verbose_name=_('contents'), through=ExamContent)


class ExcerciseContent(models.Model):
    excercise = models.ForeignKey('Excercise', verbose_name=_('excercise'))
    content = models.ForeignKey('Content', verbose_name=_('content'))


class UserExcercise(models.Model):
    user = models.ForeignKey('authentication.User', verbose_name=_('user'))
    excercise = models.ForeignKey('Excercise', verbose_name=_('excercise'))
    score = models.PositiveIntegerField(verbose_name=_('score'), default=0, null=False)


class Excercise(models.Model):
    title = models.CharField(max_length=50, verbose_name=_('title'), null=False)
    score = models.PositiveIntegerField(verbose_name=_('score'), default=0, null=False)
    deadline = models.DateTimeField(verbose_name=_('deadline'), null=False)
    description = models.CharField(max_length=1000, verbose_name=_('description'), default='', null=True)
    contents = models.ManyToManyField('Content', verbose_name=_('contents'), through=ExcerciseContent)


class NotificationContent(models.Model):
    notification = models.ForeignKey('Notification', verbose_name=_('notification'))
    content = models.ForeignKey('Content', verbose_name=_('content'))


class Notification(models.Model):
    poster = models.ForeignKey('authentication.User', verbose_name=_('poster'))
    title = models.CharField(max_length=50, verbose_name=_('title'), null=False)
    date = models.DateTimeField(verbose_name=_('date'), null=False)
    description = models.CharField(max_length=1000, verbose_name=_('description'), default='', null=True)
    contents = models.ManyToManyField('Content', verbose_name=_('contents'), through=NotificationContent)


class ContentFile(models.Model):
    content = models.ForeignKey('Content', verbose_name=_('content'))
    file = models.ForeignKey('File', verbose_name=_('file'))


class ContentTag(models.Model):
    content = models.ForeignKey('Content', verbose_name=_('content'))
    tag = models.ForeignKey('Tag', verbose_name=_('tag'))


class File(models.Model):
    file = models.FileField(verbose_name=_('file'), upload_to='contents/', null=True)
    upload_date = models.DateTimeField(verbose_name=_('upload date'), auto_now_add=timezone.now, null=False)
    description = models.CharField(max_length=1000, verbose_name=_('description'), default='', null=True)


class Tag(models.Model):
    name = models.CharField(max_length=20, verbose_name=_('name'), null=False)
    description = models.CharField(max_length=1000, verbose_name=_('description'), default='', null=True)


class Content(models.Model):
    files = models.ManyToManyField(File, verbose_name=_('files'), through=ContentFile)
    tags = models.ManyToManyField(Tag, verbose_name=_('tags'), through=ContentTag)
    description = models.CharField(max_length=1000, verbose_name=_('description'), default='', null=True)


class CourseTeachingAssistant(models.Model):
    course = models.ForeignKey('Course', verbose_name=_('course'))
    teaching_assistant = models.ForeignKey('authentication.User', verbose_name=_('teaching assistant'))


class CourseProject(models.Model):
    course = models.ForeignKey('Course', verbose_name=_('course'))
    project = models.ForeignKey('Project', verbose_name=_('project'))


class CourseExam(models.Model):
    course = models.ForeignKey('Course', verbose_name=_('course'))
    exam = models.ForeignKey('Exam', verbose_name=_('exam'))


class CourseExercise(models.Model):
    course = models.ForeignKey('Course', verbose_name=_('course'))
    excercise = models.ForeignKey('Excercise', verbose_name=_('excercise'))


class CourseNotification(models.Model):
    course = models.ForeignKey('Course', verbose_name=_('course'))
    notification = models.ForeignKey('Notification', verbose_name=_('notification'))


class CourseContent(models.Model):
    course = models.ForeignKey('Course', verbose_name=_('course'))
    content = models.ForeignKey('Content', verbose_name=_('content'))


class Course(models.Model):
    instructor = models.ForeignKey('authentication.User', verbose_name=_('instructor'))
    name = models.CharField(max_length=50, verbose_name=_('name'), null=False)
    credit = models.PositiveIntegerField(verbose_name=_('credit'), null=False)
    description = models.CharField(max_length=1000, verbose_name=_('description'), default='', null=True)

    exams = models.ManyToManyField(Exam, verbose_name=_('exams'), through=CourseExam)
    projects = models.ManyToManyField(Project, verbose_name=_('projects'), through=CourseProject)
    exercises = models.ManyToManyField(Excercise, verbose_name=_('exercises'), through=CourseExercise)
    notifications = models.ManyToManyField(Notification, verbose_name=_('notifications'), through=CourseNotification)
    contents = models.ManyToManyField('Content', verbose_name=_('contents'), through=CourseContent)
    teaching_assistants = models.ManyToManyField(
        'authentication.User', verbose_name=_('teaching assistants'),
        through=CourseTeachingAssistant, related_name='ta_course_set'
    )
