from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Habit(models.Model):
    action = models.CharField(max_length=255)
    target = models.IntegerField()
    measure = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='habits')
    created_at = models.DateField()
    updated_at = models.DateField()

class Record(models.Model):
    actual = models.IntegerField()
    date = models.DateField()
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE, related_name="records")

    class Meta:
        unique_together = [
            "user",
            "date",
        ]