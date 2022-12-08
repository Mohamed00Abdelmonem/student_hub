from django.shortcuts import render
from .models import subjecte, lesson

from django.views.generic import ListView, DetailView


# Create your views here.


def contents(request):
    return render(request, 'student/contents.html')


def control_panel(request):
    return render(request, 'student/control_panel.html')


def subject(request):
    subjects = subjecte.objects.all()
    context = {'subjects': subjects}
    return render(request, 'student/subject.html', context)


class Lessons_List(ListView):
    model = lesson


class Lesson_Detail(DetailView):
    model = lesson
