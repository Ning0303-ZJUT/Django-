from django.shortcuts import render,redirect,HttpResponse
from app01 import models
from django.db.models.query import QuerySet

from app01.utils.Pagination import Pagination
from app01.utils.bootstrap import BootstrapModelForm

class LessonTeacherForm(BootstrapModelForm):
    class Meta:
        model = models.Course #定义类
        fields = ['year','term','name','lesson_id','credit']

def lesson_teacher_list(request):
    """教师课程列表"""

    # 获取对应学期学年的对象

    year = request.POST.get('year')
    term = request.POST.get('term')
    tid = request.session['info']['id']
    # type = request.POST.get('type')
    # print(type)

    search_dict = dict()
    if year:
        search_dict['year'] = year
    if term:
        search_dict['term'] = term
    if tid:
        search_dict['teacher_id'] = tid

    queryset = models.Course.objects.filter(**search_dict).order_by("-year")
    print(queryset)
    page_obj = Pagination(request, queryset, page_size=5)
    context = {
        'queryset': page_obj.page_queryset,
        "page_string": page_obj.html(),
    }

    return render(request,'lesson_teacher_list.html', context)

def lesson_student_list(request):
    """学生课表"""
    # global queryset
    year = request.POST.get('year')
    term = request.POST.get('term')
    cls_id = request.session['info']['cls_id']

    search_dict = dict()
    if year:
        search_dict['year'] = year
    if term:
        search_dict['term'] = term
    if cls_id:
        search_dict['cls_id'] = cls_id

    queryset = models.Course.objects.filter(**search_dict).order_by("-year")
    print(queryset)
    page_obj = Pagination(request, queryset, page_size=5)
    context = {
        'queryset': page_obj.page_queryset,
        "page_string": page_obj.html(),
    }

    return render(request, 'lesson_student_list.html', context)


