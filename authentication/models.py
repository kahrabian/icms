from django.db import models
from django.contrib.auth.models import User as DjangoUser
from django.utils.translation import ugettext as _


class UserCourse(models.Model):
    user = models.ForeignKey('User', verbose_name=_('user'))
    course = models.ForeignKey('visage.Course', verbose_name=_('course'))
    score = models.PositiveIntegerField(verbose_name=_('score'), default=0, null=False)

    STATE_CHOICES = (
        ('U', _('Unknown')),
        ('P', _('Pass')),
        ('F', _('Fail')),
        ('A', _('Abscense')),
        ('R', _('Removal')),
    )
    state = models.CharField(verbose_name=_('state'), max_length=1, choices=STATE_CHOICES, default='U', null=False)


class User(models.Model):
    base_user = models.OneToOneField(DjangoUser, verbose_name=_('base user'))
    profile_photo = models.ImageField(verbose_name=_('profile photo'), upload_to='profile_photos/', null=True)
    student_number = models.CharField(max_length=10, verbose_name=_('student number'), null=True)
    entry_date = models.DateField(verbose_name=_('entry date'), null=True)

    TYPE_CHOICES = (
        ('S', _('Student')),
        ('I', _('Instructor')),
        ('T', _('Teaching Assistant')),
    )
    type = models.CharField(verbose_name=_('type'), max_length=1, choices=TYPE_CHOICES, default='S', null=False)

    SEX_CHOICES = (
        ('M', _('Male')),
        ('F', _('Female')),
    )
    sex = models.CharField(verbose_name=_('sex'), max_length=1, choices=TYPE_CHOICES, default='M', null=False)

    courses = models.ManyToManyField('visage.Course', verbose_name=_('courses'), through=UserCourse)
