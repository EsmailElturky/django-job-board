from django.urls import path , include
from . import views
from . import api

app_name='job'
urlpatterns = [
    path('',views.job_list,name="job_list"),
    path('add',views.add_job,name="add_job"),
    path('<str:slug>/',views.job_detail,name="job_detail"),

    #API
    path('api/jobs/',api.jobListApi,name="job_list_api"),
    path('api/jobs/<int:id>',api.jobDetail,name="job_detail_api"),

    ##class based view
    path('api/v2/jobs/<int:id>', api.JobDetail.as_view(), name="job_detail_api"),

]