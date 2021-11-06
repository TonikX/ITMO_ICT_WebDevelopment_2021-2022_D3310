from django.db import models


# Create your models here.
class Teacher(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    subject_types = (
        ('m', 'math'),
        ('c', 'chemical'),
        ('e', 'english'),
        ('p', 'computer science'),
    )
    subject = models.CharField(max_length=1, choices=subject_types)
    b_date = models.DateField()
    e_date = models.DateField()
    office = models.CharField(max_length=120, blank=True, null=True)


class Group(models.Model):
    number = models.CharField(max_length=120)
    head_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, blank=True, null=True)


class Classroom(models.Model):
    room_types = (
        ('b', 'base'),
        ('p', 'professional'),
    )
    room = models.CharField(max_length=1, choices=room_types)
    number = models.CharField(max_length=20)


class Schedule(models.Model):
    time = models.TimeField()
    day_types = (
        ('mon', 'monday'),
        ('tue', 'tuesday'),
        ('wed', 'wednesday'),
        ('thu', 'thursday'),
        ('fri', 'friday'),
        ('sat', 'saturday'),
    )
    day = models.CharField(max_length=3, choices=day_types)
    subject_types = (
        ('m', 'math'),
        ('c', 'chemical'),
        ('e', 'english'),
        ('p', 'computer science'),
    )
    subject = models.CharField(max_length=1, choices=subject_types)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, blank=True, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, blank=True, null=True)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, blank=True, null=True)


class Student(models.Model):
    sex_types = (
        ('m', 'male'),
        ('s', 'female'),
    )
    sex = models.CharField(max_length=1, choices=sex_types)
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    score_math = models.IntegerField(blank=True, null=True)
    score_chemical = models.IntegerField(blank=True, null=True)
    score_english = models.IntegerField(blank=True, null=True)
    score_computer = models.IntegerField(blank=True, null=True)
    semester = models.IntegerField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE, blank=True, null=True)