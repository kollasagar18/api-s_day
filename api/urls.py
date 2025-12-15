from django.urls import path
from .views import home,creating_emp

urlpatterns = [
    path("", home),
    path("home",home),
    path("creating_emp",creating_emp,name="create_emp12")
]