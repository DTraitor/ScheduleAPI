from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from typing import Optional
from .models import Group
from .serializers import GroupSerializer


@api_view(['GET'])
def search_groups(request):
    name: Optional[str] = request.GET.get('name')
    if name is None:
        return Response({"message": "No name provided"}, status=400)
    groups = Group.objects.filter(name__contains=name)
    serializer = GroupSerializer(groups, many=True)
    return Response({"groups": serializer.data, "count": len(serializer.data)})


@api_view(['GET'])
def get_group(request):
    group_id: Optional[str] = request.GET.get('id')
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
