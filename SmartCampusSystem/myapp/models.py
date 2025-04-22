from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    major = models.CharField(max_length=100, blank=True, null=True)
    role = models.CharField(
        max_length=50,
        choices=[
            ("student", "Student"),
            ("faculty", "Faculty"),
            ("admin", "Admin"),
        ],
        default="student"
    )

class Course(models.Model):
    name = models.CharField(max_length=100)
    instructor = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='courses_taught')

    def __str__(self):
        return self.name

class Enrollment(models.Model):
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    grade = models.CharField(max_length=5, blank=True, null=True)

    def __str__(self):
        return f"{self.student.username} in {self.course.name}"
