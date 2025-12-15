from django.urls import path
from .views import home,creating_emp,get_all,get_alldata

urlpatterns = [
    path("", home),
    path("creating/emp", creating_emp, name="creating_emp"),
    path("get/all", get_all,name="get_all"),
    path("get/all/data",get_alldata,name="get_alldata")
    ]

