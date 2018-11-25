from django.db import models

from django.urls import reverse, reverse_lazy, resolve
# Create your models here.


class Course(models.Model):
    course_name = models.CharField(max_length=100)
    max_degree = models.IntegerField()
    study_years = models.IntegerField()

    def __str__(self):
        return self.course_name

    def get_absolute_url(self):
        return reverse('courses')

class Student(models.Model):
    student_name = models.CharField(max_length=100)
    age = models.IntegerField()
    course = models.ManyToManyField(Course)

    def __str__(self):
        return self.student_name

    def get_absolute_url(self):
        return reverse('students')

class Grade(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    degree = models.CharField(max_length=3)

    def __str__(self):
        return self.degree

    def get_absolute_url(self):
        return reverse('grades')
