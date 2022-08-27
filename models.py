from django.db import models

# Create your models here.
class Admin(models.Model):
    """管理员"""
    username = models.CharField(verbose_name="用户名", max_length=32)
    password = models.CharField(verbose_name="密码", max_length=64)

    def __str__(self):
        return self.username

class Teacher(models.Model):
    """教师"""
    name = models.CharField(verbose_name="教师姓名", max_length=32)
    teacher_id = models.CharField(verbose_name="教师编号", max_length=32, primary_key=True)
    password = models.CharField(verbose_name="密码", max_length=64)
    # 性别约束，用元组表示可选项
    gender_choices = (
        (1, '男'),
        (2, '女'),
    )
    gender = models.SmallIntegerField(verbose_name='性别', choices=gender_choices, default=1)
    # img = models.FileField(verbose_name="证件照", max_length=128, upload_to='teacher/')

class Student(models.Model):
    """学生"""
    name = models.CharField(verbose_name="学生姓名", max_length=32)
    student_id = models.CharField(verbose_name="学号", max_length=32, primary_key=True)
    password = models.CharField(verbose_name="密码", max_length=64)
    # 性别约束，用元组表示可选项
    gender_choices = (
        (1, '男'),
        (2, '女'),
    )
    gender = models.SmallIntegerField(verbose_name='性别', choices=gender_choices, default=1)

    cls = models.ForeignKey(verbose_name="班级编号", to="Class", on_delete=models.CASCADE)
    gain_credit = models.IntegerField(verbose_name="已修学分")
    # img = models.FileField(verbose_name="证件照", max_length=128, upload_to='student/')

class Class(models.Model):
    """班级"""
    class_id = models.CharField(verbose_name="班级编号", max_length=32, primary_key=True)
    name = models.CharField(verbose_name="班级名称", max_length=64, unique=True, default="软工01")
    depart = models.CharField(verbose_name="学院", max_length=64, default="计算机学院")
    major = models.CharField(verbose_name="专业名称", max_length=64, default="软件工程")
    # stu = models.ForeignKey(verbose_name="学号" ,to="Student", to_field='id', on_delete=models.CASCADE)  #stu_id

class Course(models.Model):
    """必修课"""
    name = models.CharField(verbose_name="课程名称", max_length=64)
    lesson_id = models.CharField(verbose_name="课程编号", max_length=32, primary_key=True)
    teacher = models.ForeignKey(verbose_name="教师编号", to="Teacher", on_delete=models.CASCADE)
    cls = models.ForeignKey(verbose_name="授课班级", to="Class", on_delete=models.CASCADE)
    year = models.CharField(verbose_name="学年", max_length=64)
    term_choices = (
        (1,'(1)'),
        (2,'(2)'),
    )
    term = models.SmallIntegerField(verbose_name="学期", choices=term_choices)
    credit = models.IntegerField(verbose_name="学分")

class Selection(models.Model):
    """选修课"""
    name = models.CharField(verbose_name="课程名称", max_length=64)
    lesson_id = models.CharField(verbose_name="课程编号", max_length=32, primary_key=True)
    teacher = models.ForeignKey(verbose_name="教师编号", to="Teacher", on_delete=models.CASCADE)
    year = models.CharField(verbose_name="学年", max_length=64)
    term_choices = (
        (1, '(1)'),
        (2, '(2)'),
    )
    term = models.SmallIntegerField(verbose_name="学期", choices=term_choices)
    credit = models.IntegerField(verbose_name="学分")
    capacity = models.IntegerField(verbose_name="容量")
    is_verified = models.CharField(verbose_name="是否确认", max_length=8, default="否")
    apply_sum = models.IntegerField(verbose_name="已报名人数", default=0)

class Grade(models.Model):
    """成绩"""
    course = models.ForeignKey(verbose_name="课程编号", to="Course", on_delete=models.CASCADE)
    student = models.ForeignKey(verbose_name="学号", to="Student",  on_delete=models.CASCADE)
    grade = models.IntegerField(verbose_name="成绩")
    teacher = models.ForeignKey(verbose_name="任课老师id", to="Teacher",  on_delete=models.CASCADE)
    year = models.CharField(verbose_name="学年", max_length=64)
    term_choices = (
        (1, '(1)'),
        (2, '(2)'),
    )
    term = models.SmallIntegerField(verbose_name="学期", choices=term_choices)

class StudentSelceted(models.Model):
    """学生选择的选修课"""
    selection = models.ForeignKey(verbose_name="课程编号", to="Selection", on_delete=models.CASCADE)
    student = models.ForeignKey(verbose_name='学号', to='Student', on_delete=models.CASCADE)
    teacher = models.ForeignKey(verbose_name='教师编号', to="Teacher", on_delete=models.CASCADE)

