from django.db.models import F
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from classroom.models import Classroom
from student.models import Student, StudentInfo, GoodsUser, Goods


def addStudent(request):
    if request.method == "GET":
        return render(request,"addStudent.html")

    if request.method == "POST":
        # 添加学生信息
        stu_name = request.POST.get("name")
        if request.POST.get("sex") == "男":
            stu_sex = 1
        else:
            stu_sex = 0
        stu_birth = request.POST.get("birth")
        stu_chinese = request.POST.get("chinese")
        stu_math = request.POST.get("math")
        Student.objects.create(
            stu_name = stu_name,
            stu_sex = stu_sex,
            stu_birth = stu_birth,
            stu_chinese = stu_chinese,
            stu_math = stu_math
        )
        return render(request, "addStudent.html")

def selStudent(request):
    # 1、通过扩展表学生的地址去查找学生的信息
    # 查找 addr = 成都都江堰 的学生信息
    # （方法1）
    stus = StudentInfo.objects.filter(stu_addr='成都都江堰')
    stu = stus[0]
    selstu = Student.objects.filter(id=stu.stu_id)
    # return HttpResponse("查询成功")

    #（方法2）
    # stus = StudentInfo.objects.filter(stu_addr__contains='成都都江堰')
    # stu = stus[0]
    # selstu = stu.stu  # 根据OneToOneField来找到指定拓展表数据对应的学生数据

    # 2、通过学生表去查找学生拓展表的信息
    # 查找stu_name=刘备的学生的家庭住址
    #（方法1）
    # stu = Student.objects.filter(stu_name = "刘备").first()
    # selstu = StudentInfo.objects.filter(stu_id=stu.id)

    #（方法2）
    # stu = Student.objects.filter(stu_name="刘备").first()
    # selstu = stu.studentinfo  # 找到拓展表对应的信息
    # selstu = stu.stu_info # 较49行  二者只能存在一个
    return render(request, "selStudent.html", {'selstu': selstu})

def fselStudent(request):
    # 查询python班学生的信息
    #(方法1)
    # g = Classroom.objects.get(class_name='python')
    # stus = Student.objects.filter(classroom_id = g.id)

    #（方法2）
    # g = Classroom.objects.get(class_name='python')
    # stus = g.student_set.all() # 一对多的关系，要加_set

    # 查询王芳同学的班级信息
    # stu = Student.objects.get(stu_name='王芳')
    # gs = stu.classroom

    # 查询python班下语文成绩大于80分的学生
    # g = Classroom.objects.get(class_name='python')
    # gs = g.student_set.filter(stu_chinese__gte=80)

    # 返回python 班级中出生在2018.4.1以后的男生的信息
    # g = Classroom.objects.get(class_name='python')
    # gs = g.student_set.filter(stu_sex=True,stu_birth__gt='2018-04-01')

    #查询java班级下语文成绩超过数学成绩10分的男同学
    g = Classroom.objects.get(class_name='java')
    gs = g.student_set.filter(stu_sex=True, stu_chinese__gte=F('stu_math')+10)
    return render(request, "selClassroom.html", {'gs': gs})

def manyGoods(request):
    # 获取张飞购买的商品
    user = GoodsUser.objects.get(u_name='张飞')
    goods = user.goods_set.all()

    # 获取购买哇哈哈用户的信息
    good = Goods.objects.get(g_name="哇哈哈")
    users = good.g_user.all()
    return render(request, "goods.html", {'users': users, 'goods': goods})

def allStudents(request):
    stus = Student.objects.all()
    return render(request, "all_stus.html",{'stus':stus})


