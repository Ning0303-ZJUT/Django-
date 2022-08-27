import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, HttpResponse
from app01 import models
from app01.utils.bootstrap import BootstrapModelForm

class StudentPwdModelForm(BootstrapModelForm):
    class Meta:
        model = models.Student
        fields = ['password']


@csrf_exempt
def student_password(request):
    """学生修改密码"""
    print('pwd...')
    if request.method == 'GET':
        # form = StudentPwdModelForm(data=request)
        return render(request, "student_password.html", )
    else:
        print('post')
        stu_id = request.session['info']['id']
        input_o_pwd = request.POST.get('input_o_pwd')
        input_n_pwd = request.POST.get('input_n_pwd')
        input_s_pwd = request.POST.get('input_s_pwd')
        print(input_o_pwd)
        print(input_n_pwd)
        print(input_s_pwd)
        row_obj = models.Student.objects.filter(student_id=stu_id).first()
        print(row_obj)
        if input_o_pwd == row_obj.password:
            if input_n_pwd == input_s_pwd:
                form = StudentPwdModelForm(data={'password': input_s_pwd}, instance=row_obj)
                if form.is_valid():
                    form.save()
                    return JsonResponse({'status': True})

            else:
                return JsonResponse({'status': False, 'tips': "确认密码不一致，请重新输入。"})
        else:
            return JsonResponse({'status': False, 'tips': "原始密码错误。"})

class TeacherPwdModelForm(BootstrapModelForm):
    class Meta:
        model = models.Teacher
        fields = ['password']

def teacher_password(request):
    """教师修改密码"""
    print('pwd...')
    if request.method == 'GET':
        # form = StudentPwdModelForm(data=request)
        return render(request, "student_password.html", )
    else:
        print('post')
        teacher_id = request.session['info']['id']
        input_o_pwd = request.POST.get('input_o_pwd')
        input_n_pwd = request.POST.get('input_n_pwd')
        input_s_pwd = request.POST.get('input_s_pwd')
        print(input_o_pwd)
        print(input_n_pwd)
        print(input_s_pwd)
        row_obj = models.Teacher.objects.filter(teacher_id=teacher_id).first()
        print(row_obj)
        if input_o_pwd == row_obj.password:
            if input_n_pwd == input_s_pwd:
                form = TeacherPwdModelForm(data={'password': input_s_pwd}, instance=row_obj)
                if form.is_valid():
                    form.save()
                    return JsonResponse({'status': True})

            else:
                return JsonResponse({'status': False, 'tips': "确认密码不一致，请重新输入。"})
        else:
            return JsonResponse({'status': False, 'tips': "原始密码错误。"})
