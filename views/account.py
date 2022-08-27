from django.shortcuts import render, HttpResponse,redirect
from django import forms
from io import BytesIO

from app01 import models
from app01.utils.bootstrap import BootstrapForm
from app01.utils.code import check_code

class LoginForm(BootstrapForm):
    username = forms.CharField(
        label="用户名",
        widget=forms.TextInput,
        required=True,
    )
    password = forms.CharField(
        label="密码",
        widget=forms.PasswordInput,
        required=True,
    )
    code = forms.CharField(
        label="验证码",
        widget=forms.TextInput,
        required=True,
    )

    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        return pwd

def login(request):
    """登录"""
    if request.method == "GET":
        form = LoginForm()
        return render(request,"login.html",{'form':form})

    form = LoginForm(data=request.POST)
    if form.is_valid():
        # 验证成功 获得的用户名和密码、验证码
        # {'username':xxx,'password':xxx, 'code':xxx}
        print(form.cleaned_data)
        user_input_username = form.cleaned_data.pop('username')
        user_input_pwd = form.cleaned_data.pop('password')
        user_input_code = form.cleaned_data.pop('code')

        # 验证码的校验
        code = request.session.get('image_code', "")
        if code.upper() != user_input_code.upper():
            form.add_error("code", "验证码错误")
            return render(request, 'login.html', {'form': form})

        # 数据库校验,获取用户对象并判断用户身份，None
        if user_input_username.startswith('a') or user_input_username.startswith('A'):
            # 管理员
            account_obj = models.Admin.objects.filter(**form.cleaned_data).first()

            if not account_obj:
                form.add_error("password", "用户名或密码错误")
                return render(request, 'login.html', {'form': form})

            # 用户名和密码正确
            # 网站随机生成字符串，写到用户浏览器的cookie中，z再写入session中
            request.session["info"] = {'id': account_obj.username}
            # session 保存信息7天 = 7天免登录
            request.session.set_expiry(60 * 60 * 24 * 7)
            # return HttpResponse('success, admin.')
            return redirect('/selection/check/')

        elif user_input_username.startswith('t') or user_input_username.startswith('T'):
            # 教师
            account_obj = models.Teacher.objects.filter(teacher_id=user_input_username, password=user_input_pwd).first()
            print(account_obj)
            if not account_obj:
                form.add_error("password", "用户名或密码错误")
                return render(request, 'login.html', {'form': form})
            request.session["info"] = {'id': account_obj.teacher_id, 'name': account_obj.name}
            print(request.session['info'])
            request.session.set_expiry(60 * 60 * 24 * 7)
            # return render(request, 'lesson_teacher_list.html',{'form':form})
            return redirect('/lesson/teacher/list/')

        else:
            # 学生
            account_obj = models.Student.objects.filter(student_id=user_input_username, password=user_input_pwd).first()
            if not account_obj:
                form.add_error("password", "用户名或密码错误")
                return render(request, 'login.html', {'form': form})
            request.session["info"] = {'id': account_obj.student_id,'name':account_obj.name, 'cls_id': account_obj.cls_id}
            request.session.set_expiry(60*60*24*7)
            # return render(request, 'lesson_student_list.html',{'form':form})
            return redirect('/lesson/student/list/')

    return render(request,'login.html',{'form':form})

def image_code(request):
    """生成图片验证码"""
    img, code_string = check_code()
    print(code_string)

    # 写入session中，以便后续校验
    request.session ['image_code'] = code_string
    # 设置60s超时
    request.session.set_expiry(60)

    # 写入内存(Python3)
    stream = BytesIO()
    img.save(stream, 'png')
    return HttpResponse(stream.getvalue())


def logout(request):
    """注销"""
    request.session.clear()

    return redirect('/login/')