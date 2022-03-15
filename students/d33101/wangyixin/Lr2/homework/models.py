from django.db import models

# Create your models here.


class Student(models.Model):

    name = models.CharField(max_length=128)
    Class = models.CharField(max_length=256)
    email = models.EmailField()
    birthday = models.DateField(null=True)

    def __str__(self):
        return self.name


class Homework(models.Model):
    time_start = models.DateField()
    time_end = models.DateField(null=True)
    subject = models.CharField(max_length=30)
    desc = models.CharField(max_length=100)
    teacher = models.CharField(max_length=30)
    info = models.CharField(max_length=50)

    def __str__(self):
        return self.desc


class Studenttopic(models.Model):
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE)
    user = models.ForeignKey(Student, on_delete=models.CASCADE)
    answer = models.CharField('answer', max_length=200, default='')
    mark = models.FloatField('result', default=0)

    def __str__(self):
        return str(self.user)+'  =====  '+self.answer

