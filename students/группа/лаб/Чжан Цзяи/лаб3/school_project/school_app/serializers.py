from rest_framework import serializers
from .models import *


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"


class CreateTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"


class GroupSerializer(serializers.ModelSerializer):
    head_teacher = serializers.SlugRelatedField(read_only=True, slug_field='first_name')

    class Meta:
        model = Group
        fields = "__all__"


class CreateGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"


class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = "__all__"


class CreateClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = "__all__"


class ScheduleSerializer(serializers.ModelSerializer):
    group = serializers.SlugRelatedField(read_only=True, slug_field='number')
    classroom = serializers.SlugRelatedField(read_only=True, slug_field='number')
    teacher = serializers.SlugRelatedField(read_only=True, slug_field='first_name')

    # group = serializers.StringRelatedField(read_only=True)

    # group = GroupSerializer()
    class Meta:
        model = Schedule
        fields = "__all__"


class CreateScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = "__all__"


class StudentSerializer(serializers.ModelSerializer):
    group = serializers.SlugRelatedField(read_only=True, slug_field='number')

    class Meta:
        model = Student
        fields = "__all__"


class CreateStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
