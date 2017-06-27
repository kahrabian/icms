from django.contrib import admin
from django.contrib.auth.models import Permission

from authentication.models import User, UserCourse


admin.site.register(User)
admin.site.register(UserCourse)
admin.site.register(Permission)
