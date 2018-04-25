from django.conf.urls import url
from classroom import views
urlpatterns = [
    url(r'^grades/',views.showGrades)
]