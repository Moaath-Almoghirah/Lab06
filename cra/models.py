from django.db import models

# Create your models here.

    

class Course(models.Model):
    name = models.CharField(max_length = 50)
    
    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    student_id = models.IntegerField(primary_kay=True)
    age = models.IntegerField()
    courses = models.ManyToManyField(Course, blank=True, related_name='students')
    

    def __str__(self):
        return f'{self.name},{self.student_id},{self.courses}'
                