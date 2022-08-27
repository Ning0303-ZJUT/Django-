# Django-高校成绩管理系统
配置：Django 3.2.9 + python 3.7 + Mysql8.0.21
## 需求文档：
### 1.项目描述
高校成绩管理系统是一个记录学生和老师个人信息、上课信息、考试成绩、任课信息等一系列操作的系统。系统采用前后端不分离的开发方式，项目的功能点运用众多，且项目使用流畅。
### 2.项目需求
#### 2.1基本功能
•	教师. 
(1).查看个人信息.   
(2).输入学生成绩, 自动生成该学生已修总学分.   
(3).查看任课信息：选择学期显示结果. 
(4).修改密码：输入原密码+新密码+确认新密码，若两次输入新密码一致则修改. 
•	学生
(1).查看个人信息. 
(2).查看课表：选择学期显示结果. 
(3).查询考试成绩：选择学期显示结果. 
(4).修改密码：输入原密码+新密码+确认新密码，若两次输入新密码一致则修改. 
#### 2.2拓展需求
教师申请开设选修课，管理员审核通过，学生选择选修课。
### 3.知识点覆盖
Django框架  
Excel导入学生成绩  
Ajax异步交互  
Jquery、BootStrap  
Mysql数据库  

## 界面展示
登录界面![image](https://github.com/Ning0303-ZJUT/Django-/blob/main/img/login.png)
菜单栏![image](https://github.com/Ning0303-ZJUT/Django-/blob/main/img/menu.png)
修改密码![image](https://github.com/Ning0303-ZJUT/Django-/blob/main/img/password-modify.png)
学生信息/教师信息![image](https://github.com/Ning0303-ZJUT/Django-/blob/main/img/student-info.png)
学生选课. 
不能重复选课![image](https://github.com/Ning0303-ZJUT/Django-/blob/main/img/student-selection.png)
教师成绩上传![image](https://github.com/Ning0303-ZJUT/Django-/blob/main/img/teacher-grade-upload.png)
教师课表查询![image](https://github.com/Ning0303-ZJUT/Django-/blob/main/img/teacher-lesson-search.png)
教师选修课申报结果查询![image](https://github.com/Ning0303-ZJUT/Django-/blob/main/img/teacher-selection-search.png)
管理员选修课审核![image](https://github.com/Ning0303-ZJUT/Django-/blob/main/img/admin-selection.png)

