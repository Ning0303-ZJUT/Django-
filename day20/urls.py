"""day20 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app01.views import lesson, account, info, password, grade, selection

urlpatterns = [
    # path('admin/', admin.site.urls),

    # 登录
    path("login/", account.login),
    path("logout/", account.logout),
    path("image/code/", account.image_code),

    # 课表查询
    path('lesson/teacher/list/', lesson.lesson_teacher_list, name='lesson_teacher_list'),
    path('lesson/student/list/', lesson.lesson_student_list, name='lesson_student_list'),

    # 信息查询
    path('student/info/', info.student_info, name='student_info'),
    path('teacher/info/', info.teacher_info, name='teacher_info'),

    # 修改密码
    path('student/password/', password.student_password, name='student_password'),
    path('teacher/password/', password.teacher_password, name='teacher_password'),

    # 成绩管理
    path('grade/list/', grade.grade_list,),
    path("grade/multi/", grade.grade_multi),
    path('grade/search/', grade.grade_search, name='grade_search'),

    # 选修课
    path("selection/apply/teacher/", selection.selection_apply_teacher, name='selection_apply_teacher'),
    path("selection/list/teacher/", selection.selection_list_teacher, name='selection_list_teacher'),
    path("selection/check/", selection.selection_check, name='selection_check'),
    path("selection/<nid>/edit/", selection.selection_edit),
    path("selection/list/student/", selection.selection_list_student, name='selection_list_student'),
    path("selection/apply/student/", selection.selection_apply_student, name='selection_apply_student'),

]
