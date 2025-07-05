from django.shortcuts import render, redirect, get_object_or_404

from .models import Student, Subject, Grade, Group


def grade(request):
    subjects = Subject.objects.all()
    groups = Group.objects.all()
    return render(request, 'grade_form.html', {'subjects': subjects,
                                               'groups': groups})
