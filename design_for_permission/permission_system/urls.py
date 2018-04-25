from django.conf.urls import url
from permission_system import views

urlpatterns = [
    url(r'^checkper',views.checkPermission),
    url(r'^judgeper',views.judgePermission)
]
