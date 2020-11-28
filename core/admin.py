from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from core.models import Habit, Record, User

# Register your models here.

admin.site.register(Habit)
admin.site.register(Record)
admin.site.register(User, UserAdmin)