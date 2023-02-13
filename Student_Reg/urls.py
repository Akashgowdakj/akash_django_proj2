from django.urls import path, re_path
from Student_Reg import views


urlpatterns = [
    re_path(r'^$',views.home,name='home'),
    re_path(r'^reg',views.reg,name='reg'),
    re_path(r'^report',views.report,name='report'),

]
