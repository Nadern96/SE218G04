

from .models import Course, Student, Grade
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView , DeleteView
from django.db.models import Q
from django.core.paginator import Paginator
from django.shortcuts import  render, redirect,get_object_or_404


class HomeView(generic.ListView):
    template_name = 'Class/index.html'
    context_object_name = 'all_courses'
    def get_queryset(self):
        return Course.objects.all()




def IndexView(request):

    def get_queryset(self):
        return Course.objects.all()

    query = request.GET.get("q", None)
    all_courses = Course.objects.all()

    if query is not None:
        all_courses = all_courses.filter(course_name__startswith=query)

    context = {
        "all_courses": all_courses,
    }
    template = "Class/courses.html"
    return render(request, template, context)


class Course_DetailView(generic.DetailView):
    model = Course


class Student_DetailView(generic.DetailView):
    model = Student
    template_name = 'Class/student_detail.html'


class StudentView(generic.ListView):

    template_name = 'Class/students.html'
    context_object_name = 'all_students'

    def get_queryset(self):
        return Student.objects.all()


def GradeView(request):

    def get_queryset(self):
        return Grade.objects.all()

    query = request.GET.get("q", None)
    all_grades = Grade.objects.all()

    if query is not None:
        all_grades = all_grades.filter(student_id__student_name__startswith=query)

    context = {
        "all_grades": all_grades,
    }
    template = "Class/grades.html"
    return render(request, template, context)



class CreateCourse(CreateView):
    model = Course
    fields = ['course_name', 'max_degree', 'study_years']


class EditCourse(UpdateView):
    model = Course
    fields = ['course_name', 'max_degree', 'study_years']

def DeleteCourse(request, pk, template_name='Class/courses.html'):
    course = get_object_or_404(Course, pk=pk)
    if request.method=='POST':
        course.delete()
        return redirect('courses')
    return render(request, template_name, {'object':course})

class CreateStudent(CreateView):
    model = Student
    fields = ['student_name', 'age', 'course']


class EditStudent(UpdateView):
    model = Student
    fields = ['student_name', 'age', 'course']

def DeleteStudent (request, pk, template_name='Class/students.html'):
    student = get_object_or_404(Student, pk=pk)
    if request.method=='POST':
        student.delete()
        return redirect('students')
    return render(request, template_name, {'object':student})


class CreateGrade(CreateView):
    model = Grade
    fields = ['student_id', 'course_id', 'degree']

class EditGrade(UpdateView):
    model = Grade
    fields = ['student_id', 'course_id', 'degree']

def DeleteGrade (request, pk, template_name='Class/grades.html'):
    grade = get_object_or_404(Grade, pk=pk)
    if request.method=='POST':
        grade.delete()
        return redirect('grades')
    return render(request, template_name, {'object':grade})


#search courses by course name

