from django.db import models
#from django.contrib.auth.models import User

'''
# Create your models here.
class Department(models.Model):
    Department_name = models.CharField(max_length=30)

    def __str__(self):
        return self.Department_name


class Subject(models.Model):
    Semister = models.IntegerField()
    Subject_name = models.CharField(max_length=30)
    Subject_code = models.CharField(max_length=10)
    Full_marks = models.IntegerField()
    Pass_Marks = models.IntegerField()
    Department = models.ManyToManyField(Department)

    def __str__(self):
        return (str(self.Subject_code) + ('      ') + str(self.Subject_name))


class Student(models.Model):
    Student_registration_no = models.IntegerField()
    Batch = models.IntegerField(null=True)
    Semister = models.IntegerField(null=True)
    Student_name = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    Department = models.OneToOneField(Department, on_delete=models.CASCADE, null=True)
    Subject = models.ManyToManyField(Subject)

    def __str__(self):
        return (str(self.Student_registration_no) + str(self.Student_name))


class Teacher(models.Model):
    teacher_id = models.IntegerField()
    is_Day = models.BooleanField(default=True)
    is_Morning = models.BooleanField(default=True)
    teacher_name = models.OneToOneField(User, on_delete=models.CASCADE)
    Subject = models.ManyToManyField(Subject)

    def __str__(self):
        return (str(self.teacher_id) + ('      ') + str(self.teacher_name))


'''