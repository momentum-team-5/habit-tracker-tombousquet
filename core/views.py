from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from core.models import Habit, Record, User
from core.forms import HabitForm, RecordForm

# 5 big views, list, single, create, update, delete

def homepage(request):
    if request.user.is_authenticated:
        return redirect(to="habits_list")

    return render(request, "core/home.html")    

def habits_list(request):
    habits = Habit.objects.all()

    return render(request, "core/habits_list.html", {"habits", habits})

def habits_detail(request, pk):
    habit = get_object_or_404(request.user.habits, pk=pk)

    return render(request, "core/habits_detail.html", {"habit": habit})

@login_required
def habits_create(request):
    if request.method == "GET":
        form = HabitForm()
    else:
        form = HabitForm(data=request.POST)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.user = request.user
            habit.save()
            return redirect("habits_detail", pk=habit.pk)

    return render(request, "core/habits_create.html", {"form": form})

@login_required
def habits_update(request, habit_pk):
    habit = get_object_or_404(request.user.habits, pk=habit_pk)

    if request.method == "GET":
        form = HabitForm(instance=habit)
    else:
        form = HabitForm(instance=habit, data=request.POST)
        if form.is_valid():
            habit = form.save()
            return redirect("habits_detail", pk=habit.pk)

    return render(request, "core/habits_update.html", {"habit": habit, "form": form})

@login_required
def habits_delete(request, habit_pk):
    habit = get_object_or_404(request.user.habits, pk=habit_pk)

    if request.method == "POST":
        habit.delete()
        return redirect("habits_list")

    return render(request, "core/habits_delete.html", {"habit": habit})   

@login_required
def records_create(request, habit_pk):
    habit = get_object_or_404(request.user.habits, pk=habit_pk)

    if request.method == "GET":
        form = RecordForm()
    else:
        form = RecordForm(data=request.POST)
        if form.is_valid(): 
            record = form.save(commit=False)
            record.habit = habit
            record.save()
            return redirect(to="habits_detail", pk=habit.pk)
        
    return render(request, "core/records_create.html", {"habit": habit, "form": form})      

@login_required
def records_update(request, record_pk):
    record = get_object_or_404(Record.objects.filter(habit__user=request.user), pk=record_pk)

    if request.method == "GET":
        form = RecordForm(instance=record)
    else:
        form = RecordForm(instance=record, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("habits_detail", pk=record.habit.pk)

    return render(request, "core/records_update.html", {"record": record, "form": form})  

@login_required
def records_delete(request, record_pk):
    record = get_object_or_404(Record, pk=record_pk)

    if request.method == "POST":
        record.delete()
        return redirect("habits_detail")

    return render(request, "core/records_delete.html", {"record": record, })       