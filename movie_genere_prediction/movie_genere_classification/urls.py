from django.urls import path
from . import views

urlpatterns = [
    path('',views.mainpage,name="mainpage"),
    path('predict',views.predict,name="predict"),
]