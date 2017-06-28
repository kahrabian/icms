from django.db import models
from django.utils.translation import ugettext as _
from django.utils import timezone


class ProjectContent(models.Model):
    project = models.ForeignKey('Project', verbose_name=_('project'))
    content = models.ForeignKey('Content', verbose_name=_('content'))

    class Meta:
        verbose_name = _('project content')
        verbose_name_plural = _('project contents')


class UserProject(models.Model):
    user = models.ForeignKey('authentication.User', verbose_name=_('user'))
    project = models.ForeignKey('Project', verbose_name=_('project'))
    score = models.PositiveIntegerField(verbose_name=_('score'), default=0, null=False)

    class Meta:
        verbose_name = _('user project')
        verbose_name_plural = _('user projects')


class Project(models.Model):
    title = models.CharField(max_length=50, verbose_name=_('title'), null=False)
    score = models.PositiveIntegerField(verbose_name=_('score'), default=0, null=False)
    deadline = models.DateTimeField(verbose_name=_('deadline'), null=False)
    description = models.CharField(max_length=1000, verbose_name=_('description'), default='', null=True)
    contents = models.ManyToManyField('Content', verbose_name=_('contents'), through=ProjectContent)

    class Meta:
        verbose_name = _('project')
        verbose_name_plural = _('projects')


class ExamContent(models.Model):
    exam = models.ForeignKey('Exam', verbose_name=_('exam'))
    content = models.ForeignKey('Content', verbose_name=_('content'))

    class Meta:
        verbose_name = _('exam content')
        verbose_name_plural = _('exam contents')


class UserExam(models.Model):
    user = models.ForeignKey('authentication.User', verbose_name=_('user'))
    exam = models.ForeignKey('Exam', verbose_name=_('exam'))
    score = models.PositiveIntegerField(verbose_name=_('score'), default=0, null=False)

    class Meta:
        verbose_name = _('user exam')
        verbose_name_plural = _('user exams')


class Exam(models.Model):
    title = models.CharField(max_length=50, verbose_name=_('title'), null=False)
    score = models.PositiveIntegerField(verbose_name=_('score'), default=0, null=False)
    date = models.DateTimeField(verbose_name=_('date'), null=False)
    description = models.CharField(max_length=1000, verbose_name=_('description'), default='', null=True)
    contents = models.ManyToManyField('Content', verbose_name=_('contents'), through=ExamContent)

    class Meta:
        verbose_name = _('exam')
        verbose_name_plural = _('exams')


class ExcerciseContent(models.Model):
    excercise = models.ForeignKey('Excercise', verbose_name=_('excercise'))
    content = models.ForeignKey('Content', verbose_name=_('content'))

    class Meta:
        verbose_name = _('excercise content')
        verbose_name_plural = _('excercise contents')


class UserExcercise(models.Model):
    user = models.ForeignKey('authentication.User', verbose_name=_('user'))
    excercise = models.ForeignKey('Excercise', verbose_name=_('excercise'))
    score = models.PositiveIntegerField(verbose_name=_('score'), default=0, null=False)

    class Meta:
        verbose_name = _('user excercise')
        verbose_name_plural = _('user excercises')


class Excercise(models.Model):
    title = models.CharField(max_length=50, verbose_name=_('title'), null=False)
    score = models.PositiveIntegerField(verbose_name=_('score'), default=0, null=False)
    deadline = models.DateTimeField(verbose_name=_('deadline'), null=False)
    description = models.CharField(max_length=1000, verbose_name=_('description'), default='', null=True)
    contents = models.ManyToManyField('Content', verbose_name=_('contents'), through=ExcerciseContent)

    class Meta:
        verbose_name = _('excercise')
        verbose_name_plural = _('excercises')


class NotificationContent(models.Model):
    notification = models.ForeignKey('Notification', verbose_name=_('notification'))
    content = models.ForeignKey('Content', verbose_name=_('content'))

    class Meta:
        verbose_name = _('notification content')
        verbose_name_plural = _('notification contents')


class Notification(models.Model):
    poster = models.ForeignKey('authentication.User', verbose_name=_('poster'))
    title = models.CharField(max_length=50, verbose_name=_('title'), null=False)
    date = models.DateTimeField(verbose_name=_('date'), null=False)
    description = models.CharField(max_length=1000, verbose_name=_('description'), default='', null=True)
    contents = models.ManyToManyField('Content', verbose_name=_('contents'), through=NotificationContent)

    class Meta:
        verbose_name = _('notification')
        verbose_name_plural = _('notifications')


class ContentFile(models.Model):
    content = models.ForeignKey('Content', verbose_name=_('content'))
    file = models.ForeignKey('File', verbose_name=_('file'))

    class Meta:
        verbose_name = _('content file')
        verbose_name_plural = _('content files')


class ContentTag(models.Model):
    content = models.ForeignKey('Content', verbose_name=_('content'))
    tag = models.ForeignKey('Tag', verbose_name=_('tag'))

    class Meta:
        verbose_name = _('content tag')
        verbose_name_plural = _('content tags')


class File(models.Model):
    file = models.FileField(verbose_name=_('file'), upload_to='contents/', null=True)
    upload_date = models.DateTimeField(verbose_name=_('upload date'), auto_now_add=timezone.now, null=False)
    description = models.CharField(max_length=1000, verbose_name=_('description'), default='', null=True)

    class Meta:
        verbose_name = _('file')
        verbose_name_plural = _('files')


class Tag(models.Model):
    name = models.CharField(max_length=20, verbose_name=_('name'), null=False)
    description = models.CharField(max_length=1000, verbose_name=_('description'), default='', null=True)

    class Meta:
        verbose_name = _('tag')
        verbose_name_plural = _('tags')


class Content(models.Model):
    files = models.ManyToManyField(File, verbose_name=_('files'), through=ContentFile)
    tags = models.ManyToManyField(Tag, verbose_name=_('tags'), through=ContentTag)
    description = models.CharField(max_length=1000, verbose_name=_('description'), default='', null=True)

    class Meta:
        verbose_name = _('content')
        verbose_name_plural = _('contents')


class CourseTeachingAssistant(models.Model):
    course = models.ForeignKey('Course', verbose_name=_('course'))
    teaching_assistant = models.ForeignKey('authentication.User', verbose_name=_('teaching assistant'))

    class Meta:
        verbose_name = _('course teaching assistant')
        verbose_name_plural = _('course teaching assistants')


class CourseProject(models.Model):
    course = models.ForeignKey('Course', verbose_name=_('course'))
    project = models.ForeignKey('Project', verbose_name=_('project'))

    class Meta:
        verbose_name = _('course project')
        verbose_name_plural = _('course projects')


class CourseExam(models.Model):
    course = models.ForeignKey('Course', verbose_name=_('course'))
    exam = models.ForeignKey('Exam', verbose_name=_('exam'))

    class Meta:
        verbose_name = _('course exam')
        verbose_name_plural = _('course exams')


class CourseExercise(models.Model):
    course = models.ForeignKey('Course', verbose_name=_('course'))
    excercise = models.ForeignKey('Excercise', verbose_name=_('excercise'))

    class Meta:
        verbose_name = _('course excercise')
        verbose_name_plural = _('course excercises')


class CourseNotification(models.Model):
    course = models.ForeignKey('Course', verbose_name=_('course'))
    notification = models.ForeignKey('Notification', verbose_name=_('notification'))

    class Meta:
        verbose_name = _('course notification')
        verbose_name_plural = _('course notifications')


class CourseContent(models.Model):
    course = models.ForeignKey('Course', verbose_name=_('course'))
    content = models.ForeignKey('Content', verbose_name=_('content'))

    class Meta:
        verbose_name = _('course content')
        verbose_name_plural = _('course contents')


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

    class Meta:
        verbose_name = _('course')
        verbose_name_plural = _('courses')
