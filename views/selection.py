from django.shortcuts import render, HttpResponse,redirect
from django import forms
from io import BytesIO

from app01.utils.Pagination import Pagination
from app01 import models
from django.http import JsonResponse
from app01.utils.bootstrap import BootstrapModelForm

class SelectionModelForm(BootstrapModelForm):
    class Meta:
        model = models.Selection
        exclude = ['teacher_id', 'is_verified', 'apply_sum']


def selection_list_teacher(request):
    """教师选修课申报结果查询"""
    # 搜索
    data_dict = {}
    search_data = request.GET.get('q', "")
    teacher_id = request.session['info']['id']
    data_dict['teacher_id'] = teacher_id
    if search_data:
        data_dict['name__contains'] = search_data

    year = request.POST.get('year')
    term = request.POST.get('term')
    if year:
        data_dict['year'] = year
    if term:
        data_dict['term'] = term

    # 根据条件获取数据
    queryset = models.Selection.objects.filter(**data_dict).order_by("-year")
    page_obj = Pagination(request,queryset)
    context = {
        'queryset': page_obj.page_queryset, # 分完页的数据
        "search_data": search_data,
        "page_string": page_obj.html()  # 页码
    }
    return render(request,'selection_list_teacher.html', context)

def selection_apply_teacher(request):
    """教师选修课申报"""
    if request.method == "GET":
        form = SelectionModelForm()
        return render(request, 'selection_apply_teacher.html', {'form': form})
    form = SelectionModelForm(data=request.POST)
    if form.is_valid():
        selection = form.save(commit=False)  # 手动设置其他必填字段
        selection.teacher_id = request.session['info']['id']
        selection.save()
        return redirect('/selection/list/teacher/')
    return render(request, 'selection_apply_teacher.html', {'form': form})

def selection_check(request):
    """管理员审核列表"""
    # 搜索
    data_dict = {}
    search_data = request.GET.get('q', "")
    if search_data:
        data_dict['name__contains'] = search_data

    year = request.POST.get('year')
    term = request.POST.get('term')
    if year:
        data_dict['year'] = year
    if term:
        data_dict['term'] = term

    # 根据条件获取数据
    queryset = models.Selection.objects.filter(**data_dict).order_by("-year")
    page_obj = Pagination(request, queryset)
    context = {
        'queryset': page_obj.page_queryset, # 分完页的数据
        "search_data": search_data,
        "page_string": page_obj.html()  # 页码
    }
    return render(request,'selection_check.html', context)

class SelectionEditModelForm(BootstrapModelForm):
    class Meta:
        model = models.Selection
        exclude = ['apply_sum']

def selection_edit(request, nid):
    """管理员编辑上报的选修课"""
    row_obj = models.Selection.objects.filter(lesson_id=nid).first()

    if request.method == "GET":
        form = SelectionEditModelForm(instance=row_obj)
        return render(request, "selection_edit.html", {'form': form})

    form = SelectionEditModelForm(data=request.POST, instance=row_obj)
    if form.is_valid():
        form.save()
        return redirect('/selection/check/')

    return render(request, "selection_edit.html", {'form': form})

def selection_list_student(request):
    """学生选修课查询"""
    # 搜索
    data_dict = {}
    search_data = request.GET.get('q', "")
    data_dict['is_verified'] = "是"
    if search_data:
        data_dict['name__contains'] = search_data

    # 根据学期查询
    year = request.POST.get('year')
    term = request.POST.get('term')
    if year:
        data_dict['year'] = year
    if term:
        data_dict['term'] = term

    student_id = request.session['info']['id']

    # 获取已选择的对象
    queryset_selected = models.StudentSelceted.objects.filter(student_id=student_id)
    list1 = []
    for data in queryset_selected:
        list1.append(data.selection_id)
    # print(list1)

    # 根据条件获取数据
    queryset = models.Selection.objects.filter(**data_dict).order_by("-year")
    page_obj = Pagination(request, queryset)
    context = {
        'queryset': page_obj.page_queryset, # 分完页的数据
        "search_data": search_data,
        "page_string": page_obj.html(),  # 页码
        "selected_list": list1,
    }
    return render(request, 'selection_list_student.html', context)

def selection_apply_student(request):
    """学生报名选修课"""
    student_id = request.session['info']['id']
    uid = request.GET.get('uid')
    row_obj = models.Selection.objects.get(lesson_id=uid)
    current = row_obj.apply_sum
    teacher_id = row_obj.teacher_id
    print(current)
    capacity = row_obj.capacity
    print(capacity)
    if current >= capacity:
        return JsonResponse({'status': False, 'error': "名额已满,报名失败。"})

    # 报名成功
    row_obj.apply_sum = current + 1
    print((row_obj.apply_sum))
    row_obj.save()
    models.StudentSelceted.objects.create(selection_id=uid, student_id=student_id, teacher_id=teacher_id)
    return JsonResponse({'status': True})



