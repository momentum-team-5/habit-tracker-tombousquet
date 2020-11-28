from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Habit(models.Model):
    action = models.CharField(max_length=255)
    target = models.IntegerField()
    measure = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='habits')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Record(models.Model):
    actual = models.IntegerField()
    date = models.DateField()
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE, related_name="records")

    class Meta:
        unique_together = [
            "habit",
            "date",
        ]