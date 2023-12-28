from datetime import date, timedelta
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from typing import Optional
from .models import Group, Lesson
from .serializers import GroupSerializer, LessonSerializer


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
    if (name is None or short_name is None or description is None or teacher is None or link is None or location is None
            or kind is None or repeat_type is None or repeat_interval is None):
        return Response({"message": "No lesson data provided"}, status=400)

    lesson = Lesson.objects.create(
        name=name, short_name=short_name, description=description, teacher=teacher, link=link,
        location=location, kind=kind, repeat_type=repeat_type, repeat_interval=repeat_interval
    )
    group.lessons.add(lesson)
    group_serializer = GroupSerializer(group)
    lesson_serializer = LessonSerializer(lesson)
    return Response({"group": group_serializer.data, "lesson": lesson_serializer.data})


@api_view(['DEL'])
def delete_lesson(request):
    group_id: Optional[str] = request.data.get('group_id')
    if group_id is None:
        return Response({"message": "No group_id provided"}, status=400)
    group = Group.objects.get(id=group_id)
    if group is None:
        return Response({"message": "No group found"}, status=404)
    lesson_id: Optional[str] = request.data.get('lesson_id')
    if lesson_id is None:
        return Response({"message": "No lesson_id provided"}, status=400)
    lesson = Lesson.objects.get(id=lesson_id)
    if lesson is None:
        return Response({"message": "No lesson found"}, status=404)
    group.lessons.remove(lesson)
    group_serializer = GroupSerializer(group)
    lesson_serializer = LessonSerializer(lesson)
    return Response({"group": group_serializer.data, "lesson": lesson_serializer.data})


@api_view(['GET'])
def get_lessons_at_date(request):
    group_id: Optional[str] = request.query_params.get('group_id')
    if group_id is None:
        return Response({"message": "No group_id provided"}, status=400)
    group = Group.objects.get(id=group_id)
    if group is None:
        return Response({"message": "No group found"}, status=404)
    date_string: Optional[str] = request.query_params.get('date')
    if date_string is None:
        return Response({"message": "No date provided"}, status=400)
    try:
        current_date: date = date.fromisoformat(date_string)
    except ValueError:
        return Response({"message": "Invalid date format"}, status=400)
    lessons = []
    # Get lessons that repeat on this date
    for lesson in group.lessons.filter(
            repeat_type__isnull=False, repeat_interval__isnull=False
    ):
        delta: timedelta = current_date - lesson.start_time.date()
        match lesson.repeat_type:
            case Lesson.RepeatType.EVERY_YEAR:
                if ((current_date.year - lesson.start_time.year) % lesson.repeat_interval) == 0 and \
                        lesson.start_time.month == current_date.month and lesson.start_time.day == current_date.day:
                    lessons.append(lesson)
            case Lesson.RepeatType.EVERY_MONTH:
                months = (((current_date.year - lesson.start_time.year) * 12)
                          + (current_date.month - lesson.start_time.month))
                if (months % lesson.repeat_interval) == 0 and lesson.start_time.day == current_date.day:
                    lessons.append(lesson)
            case Lesson.RepeatType.EVERY_WEEK:
                weeks = delta.days // 7
                if (weeks % lesson.repeat_interval) == 0 and lesson.start_time.weekday() == current_date.weekday():
                    lessons.append(lesson)
            case Lesson.RepeatType.EVERY_DAY:
                if (delta.days % lesson.repeat_interval) == 0:
                    lessons.append(lesson)

    serializer = LessonSerializer(lessons, many=True)
    return Response({
        "group": GroupSerializer(group).data,
        "lessons": serializer.data,
        "count": len(serializer.data)
    })
