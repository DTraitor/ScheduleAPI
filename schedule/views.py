from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from typing import Optional
from .models import Group
from .serializers import GroupSerializer


@api_view(['GET'])
def search_groups(request):
    name: Optional[str] = request.query_params.get('name')
    if name is None:
        return Response({"message": "No name provided"}, status=400)
    groups = Group.objects.filter(name__contains=name)
    serializer = GroupSerializer(groups, many=True)
    return Response({"groups": serializer.data, "count": len(serializer.data)})


@api_view(['GET'])
def get_group(request):
    group_id: Optional[str] = request.query_params.get('id')
    if group_id is None:
        return Response({"message": "No id provided"}, status=400)
    group = Group.objects.get(id=group_id)
    if group is None:
        return Response({"message": "No group found"}, status=404)
    serializer = GroupSerializer(group)
    return Response(serializer.data)


@api_view(['POST'])
def create_group(request):
    name: Optional[str] = request.data.get('name')
    short_name: Optional[str] = request.data.get('short_name')
    if name is None or short_name is None:
        return Response({"message": "No name and no short_name provided"}, status=400)
    group = Group.objects.create(name=name, short_name=short_name)
    serializer = GroupSerializer(group)
    return Response(serializer.data)


@api_view(['DEL'])
def delete_group(request):
    group_id: Optional[str] = request.data.get('id')
    if group_id is None:
        return Response({"message": "No id provided"}, status=400)
    group = Group.objects.get(id=group_id)
    if group is None:
        return Response({"message": "No group found"}, status=404)
    group.delete()
    return Response({"message": "Group deleted"})


@api_view(['POST'])
def add_lesson(request):
    group_id: Optional[str] = request.data.get('group_id')
    if group_id is None:
        return Response({"message": "No group_id provided"}, status=400)
    group = Group.objects.get(id=group_id)
    if group is None:
        return Response({"message": "No group found"}, status=404)
    name: Optional[str] = request.data.get('name')
    short_name: Optional[str] = request.data.get('short_name')
    description: Optional[str] = request.data.get('description')
    teacher: Optional[str] = request.data.get('teacher')
    link: Optional[str] = request.data.get('link')
    location: Optional[str] = request.data.get('location')
    kind: Optional[int] = request.data.get('kind')
    repeat_type: Optional[int] = request.data.get('repeat_type')
    repeat_interval: Optional[int] = request.data.get('repeat_interval')
    if name is None or short_name is None or description is None or teacher is None or link is None or location is None or kind is None or repeat_type is None or repeat_interval is None:
        return Response({"message": "No lesson data provided"}, status=400)
