from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('log/',views.log,name="taskLog"),
    path('delTask/',views.delTask,name='delTask'),
    path('editTask/',views.editTask,name='editTask'),
    path('signup/',views.signUp,name='signUp'),
    path('login/',views.logIn,name='logIn'),
    path('logout/',views.logOut,name='logOut'),
]