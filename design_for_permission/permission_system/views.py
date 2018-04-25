from django.shortcuts import render

# Create your views here.
from permission_system.models import Role, User, Permission


def checkPermission(request):
    if request.method == "GET":
        return render(request,"inputUser.html")
    if request.method == "POST":
        name = request.POST.get("name")
        user = User.objects.get(u_name=name)
        role = Role.objects.get(id=user.r_id)
        pers = role.permission_set.all()
        return render(request,"showPermission.html",{'pers':pers})

def judgePermission(request):
    if request.method == "GET":
        return render(request,"querySpecificPermission.html")
    if request.method == "POST":
        name = request.POST.get("name")
        per = request.POST.get("permission")

        user = User.objects.get(u_name=name)
        role = Role.objects.get(id=user.r_id)
        pers = role.permission_set.filter(p_name=per)

        return render(request, "showResult.html", {'pers': pers})