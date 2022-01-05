from rest_framework import generics, status
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.response import Response


class SkillAPIView(APIView):
    def get(self, request):
        skills = Skill.objects.all()
        serializer = SkillSerializer(skills, many=True)
        return Response({"Skills": serializer.data})


class SkillCreateAPIView(APIView):
    serializer_class = SkillCreateSerializer
    queryset = Skill.objects.all()


class WarriorListAPIView(generics.ListAPIView):
    serializer_class = WarriorNestedSerializer
    queryset = Warrior.objects.all()


class ProfessionCreateAPIView(generics.CreateAPIView):
    serializer_class = ProfessionCreateSerializer
    queryset = Profession.objects.all()


class WarriorAPIView(APIView):
    def get(self, request):
        warriors = Warrior.objects.all()
        ser = WarriorSerializer(instance=warriors, many=True)
        return Response(ser.data, status=200)

    def post(self, request):  # 添加数据
        ser = WarriorSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=200)
        return Response(ser.errors)


class WarriorSingleView(APIView):
    def get(self, request, pk):
        warrior = Warrior.objects.get(id=pk)
        ser = WarriorSerializers(instance=warrior)
        return Response(ser.data)

    def put(self, request, pk):  # 修改
        warrior = Warrior.objects.get(pk=pk)
        ser = WarriorSerializers(instance=warrior, data=request.data)  # 注意指定参数
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=200)
        return Response(ser.errors)

    def delete(self, request, pk):
        Warrior.objects.get(pk=pk).delete()
        return Response(status=status.HTTP_200_OK)


class WarriorAllView(generics.ListAPIView):
    def get(self, request, pk):
        warrior = Warrior.objects.get(id=pk)
        ser = WarriorNestedSerializer(instance=warrior)
        return Response(ser.data)
