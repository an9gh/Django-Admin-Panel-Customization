from django.urls import path

from app import views



urlpatterns = [
    path('',views.job_list,name='index'),
    path('hello/',views.hello,name='hello'),
    path('job/<int:id>/',views.job_detail,name='job_detail'),
]
