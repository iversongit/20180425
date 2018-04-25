from django.conf.urls import url
from student import views

urlpatterns = [
    url(r'^addstu',views.addStudent),
    url(r'^selstu',views.selStudent),
    url(r'^fselstu',views.fselStudent),
    url(r'^manygoods',views.manyGoods),
    url(r'^stu',views.allStudents)
]