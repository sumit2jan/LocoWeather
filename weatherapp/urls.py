from django.urls import path
from . import  views

urlpatterns = [
    path('',views.index,name='home'),
    path('ai/',views.baseai,name="ai"),
    path('coming-soon/',views.comingsoon,name="cum")
]
