from django.urls import path
from . import views

urlpatterns = [
  path("", views.home, name="home"), 
  #path("login/", views.login_user, name="login"),  
  path("logout/", views.logout_user, name="logout"),  
  path("register/", views.register_user, name="register"), 
  path("habit/<int:pk>", views.habit_record, name="habit"), 
  path("delete_habit/<int:pk>", views.delete_habit, name="delete_habit"), 
  path("add_habit/", views.add_habit, name="add_habit"), 
  path("add_habit/", views.add_habit, name="add_habit"), 
   
]