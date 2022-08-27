from django.shortcuts import render,redirect,HttpResponse
from app01 import models
from django.http import JsonResponse
from app01.utils.bootstrap import BootstrapModelForm
from app01.utils.Pagination import Pagination



class StudentInfoModelForm(BootstrapModelForm):
    class Meta:
        model = models.Student
        exclude = ['cls']

def student_info(request):
    """根据学号获取学生信息"""
    stu_id = request.session['info']['id']
    row_obj = models.Student.objects.filter(student_id=stu_id).first()
    form = StudentInfoModelForm(instance=row_obj)
    return render(request, "student_info.html", {'form':form})


class TeacherInfoModelForm(BootstrapModelForm):
    class Meta:
        model = models.Teacher
        fields = "__all__"

def teacher_info(request):
    """根据教师编号获取教师信息"""
    teacher_id = request.session['info']['id']
    row_obj = models.Teacher.objects.filter(teacher_id=teacher_id).first()
    form = TeacherInfoModelForm(instance=row_obj)
    return render(request, "teacher_info.html", {'form': form})



