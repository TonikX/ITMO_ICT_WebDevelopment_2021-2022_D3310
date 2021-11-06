from rest_framework import generics, status
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.response import Response
from django.db.models import Avg, Sum, Count


class TeacherListView(generics.ListAPIView):
    serializer_class = TeacherSerializer

    def get_queryset(self):
        queryset = Teacher.objects.all()

        params = self.request.query_params

        subject = params.get('subject', None)

        if subject:
            queryset = queryset.filter(subject__exact=subject)

        return queryset


class TeacherRetrieveView(generics.RetrieveAPIView):
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()


class TeacherCreateView(generics.CreateAPIView):
    serializer_class = CreateTeacherSerializer
    queryset = Teacher.objects.all()


class TeacherUpdateView(generics.UpdateAPIView):
    serializer_class = CreateTeacherSerializer
    queryset = Teacher.objects.all()


class TeacherCountView(APIView):
    def get(self, request):
        counts_m = Teacher.objects.filter(subject='m').count()
        counts_e = Teacher.objects.filter(subject='e').count()
        counts_c = Teacher.objects.filter(subject='c').count()
        counts_p = Teacher.objects.filter(subject='p').count()
        return Response({
            "Общие преподаватель компьютера": counts_m,
            "Общие преподаватель матиматики": counts_e,
            "Общие преподаватель англиские": counts_c,
            "Общие преподаватель химия": counts_p,
                         }
                        )


class GroupListView(generics.ListAPIView):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()


class GroupRetrieveView(generics.RetrieveAPIView):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()


class GroupCreateView(generics.CreateAPIView):
    serializer_class = CreateGroupSerializer
    queryset = Group.objects.all()


class GroupUpdateView(generics.UpdateAPIView):
    serializer_class = CreateGroupSerializer
    queryset = Group.objects.all()


class ClassroomListView(generics.ListAPIView):
    serializer_class = ClassroomSerializer

    def get_queryset(self):
        queryset = Classroom.objects.all()

        params = self.request.query_params

        room = params.get('room', None)
        if room:
            queryset = queryset.filter(room__exact=room)

        return queryset


class ClassroomRetrieveView(generics.RetrieveAPIView):
    serializer_class = ClassroomSerializer
    queryset = Classroom.objects.all()


class ClassroomCreateView(generics.CreateAPIView):
    serializer_class = CreateClassroomSerializer
    queryset = Classroom.objects.all()


class ClassroomUpdateView(generics.UpdateAPIView):
    serializer_class = CreateClassroomSerializer
    queryset = Classroom.objects.all()


class ClassroomCountBaseView(APIView):
    def get(self, request):
        count_base = Classroom.objects.filter(room='b').count()
        count_profession = Classroom.objects.filter(room='p').count()
        return Response({
            "Общие  базовые": count_base,
            "Общие профильные": count_profession
        }
        )


class ScheduleListView(generics.ListAPIView):
    serializer_class = ScheduleSerializer

    def get_queryset(self):
        queryset = Schedule.objects.all()

        params = self.request.query_params

        day = params.get('day', None)
        group = params.get('group', None)
        subject = params.get('subject', None)
        if day:
            queryset = queryset.filter(day__exact=day)
        if subject:
            queryset = queryset.filter(subject__exact=subject)
        if group:
            queryset = queryset.filter(group__number=group)

        return queryset


class ScheduleRetrieveView(generics.RetrieveAPIView):
    serializer_class = ScheduleSerializer
    queryset = Schedule.objects.all()


class ScheduleCreateView(generics.CreateAPIView):
    serializer_class = CreateScheduleSerializer
    queryset = Schedule.objects.all()


class ScheduleUpdateView(generics.UpdateAPIView):
    serializer_class = CreateScheduleSerializer
    queryset = Schedule.objects.all()


class StudentListView(generics.ListAPIView):
    serializer_class = StudentSerializer

    def get_queryset(self):
        queryset = Student.objects.all()

        params = self.request.query_params

        group = params.get('group', None)
        sex = params.get('sex', None)
        if sex:
            queryset = queryset.filter(sex__exact=sex)
        if group:
            queryset = queryset.filter(group__number=group)

        return queryset


class StudentRetrieveView(generics.RetrieveAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()


class StudentCreateView(generics.CreateAPIView):
    serializer_class = CreateStudentSerializer
    queryset = Student.objects.all()


class StudentUpdateView(generics.UpdateAPIView):
    serializer_class = CreateStudentSerializer
    queryset = Student.objects.all()


class StudentCountGirlView(APIView):
    def get(self, request, pk):
        count_girls = Student.objects.filter(group=pk, sex='s').count()
        counts_boys = Student.objects.filter(group=pk, sex='m').count()
        return Response(
            {"Общие студентки": count_girls,
             "Общие студенты": counts_boys,
             }
        )


class ReportView(APIView):
    def get(self, request, pk):
        aver_grades = Student.objects.filter(group=pk).aggregate(Avg('score_math'),
                                                                 Avg('score_chemical'),
                                                                 Avg('score_english'),
                                                                 Avg('score_computer'))
        all_people = Student.objects.filter(group=pk).aggregate(Count('last_name'))
        head_teacher = Group.objects.filter(id=pk)
        serializer = GroupSerializer(head_teacher, many=True)

        return Response({
            'Средний балл': aver_grades,
            'Обшие люди': all_people,
            'руководитель': serializer.data,
        }
        )
