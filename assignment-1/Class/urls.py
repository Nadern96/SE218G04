"""School_Assignment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import  url
from django.urls import path
from . import views

urlpatterns = [
# /Class
    url(r'^$', views.HomeView.as_view(), name='index'),
#/Class/coueses
    url(r'^courses/$', views.IndexView, name='courses'),
#/Class/students
    url(r'^students/$', views.StudentView.as_view(), name='students'),
#/Class/grades
    url(r'^grades/$', views.GradeView, name='grades'),

# /Class/courses/id/detail

    url(r'^courses/(?P<pk>[0-9]+)/details$', views.Course_DetailView.as_view(), name="course_detail"),

# /Class/<students/id/
    url(r'^students/(?P<pk>[0-9]+)/details$', views.Student_DetailView.as_view(), name="student_detail"),

# /Class/courses/add
    url(r'^courses/add/$', views.CreateCourse.as_view(), name="course-add"),

# /Class/courses/2
    url(r'^courses/(?P<pk>[0-9]+)/$', views.EditCourse.as_view(), name="course-edit"),

# /Class/courses/2/delete
    path('delete/<int:pk>/course', views.DeleteCourse, name='DeleteCourse'),


# /Class/students/add/
    url(r'^students/add/$', views.CreateStudent.as_view(), name="student-add"),

# /Class/students/2/
    url(r'^students/(?P<pk>[0-9]+)/$', views.EditStudent.as_view(), name="student-edit"),

# /Class/students/2/delete
    path('delete/<int:pk>/student', views.DeleteStudent, name='DeleteStudent'),


# /Class/grades/add/
    url(r'^grades/add/$', views.CreateGrade.as_view(), name="grade-add"),

# /Class/grades/2/
    url(r'^grades/(?P<pk>[0-9]+)/$', views.EditGrade.as_view(), name="grade-edit"),

# /Class/grades/2/delete
    path('delete/<int:pk>/grade', views.DeleteGrade, name='DeleteGrade'),

#/Class/courses/


]

