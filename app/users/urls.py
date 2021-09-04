from django.urls import path

from . import views

urlpatterns = [

    path('all/', views.AllUsers.as_view()),
    path('<int:id>/', views.SpecificUser.as_view()),

]