from django.shortcuts import render
from school.models import Student

def students_list(request):
    template = 'school/students_list.html'
    students = Student.objects.all().order_by('group')
    context = {'students': students}
    return render(request, template, context)