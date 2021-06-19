from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [

    # ****************** workshops urls ****************** 
    path('', views.WorkshopList.as_view()),
    path('<int:pk>/', views.WorkshopDetail.as_view()),

    # ****************** employees urls ****************** 
    path('<int:pk>/employees/', views.EmployeeList.as_view()),
    path('<int:pk>/employees/<int:employee_pk>/', views.EmployeeDetail.as_view()),

    # ****************** tasks urls ****************** 
    path('<int:pk>/tasks/', views.TaskList.as_view()),
    path('<int:pk>/tasks/<int:task_pk>/', views.TaskDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

