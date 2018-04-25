from django.db import models

# Create your models here.
from classroom.models import Classroom


class Student(models.Model):
    stu_name = models.CharField(max_length=10)
    stu_sex = models.BooleanField()
    stu_birth = models.DateField()
    stu_create_time = models.DateTimeField(auto_now_add=True)
    stu_operate_time = models.DateTimeField(auto_now=True)
    stu_chinese = models.DecimalField(max_digits=3,decimal_places=1)
    stu_math = models.DecimalField(max_digits=3,decimal_places=1)
    classroom = models.ForeignKey(Classroom,null=True)


    class Meta:
        db_table = "student"

class StudentInfo(models.Model):  # 扩充Student的信息
    stu_addr = models.CharField(max_length=30)
    stu_age = models.IntegerField()
    stu = models.OneToOneField(Student,
                               on_delete=models.CASCADE,
                               related_name= "stu_info")

    class Meta:
        db_table = "student_info"

class GoodsUser(models.Model):
    u_name = models.CharField(max_length=10)
    class Meta:
        db_table = "good_user"

class Goods(models.Model):
    g_name = models.CharField(max_length=10)
    g_user = models.ManyToManyField(GoodsUser)

    class Meta:
        db_table = "goods"
