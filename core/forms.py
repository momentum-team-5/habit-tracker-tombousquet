from django import forms
from core.models import Habit, Record, User

class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = [
            'action',
            'target',
            'measure',
        ]

class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = [
            'actual',
            'date',
        ]