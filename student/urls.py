from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name = 'index'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name = 'login'),
    path('dashboard/',views.dashboard,name = 'dashboard'),
    path('signout/',views.signout,name = 'signout'),
    path('add_student',views.add_student,name = 'add_student'),
    path('view_student/<int:pk>',views.view_student,name = 'view_student'),
    path('delete_student/<int:pk>',views.delete_student,name = 'delete_student'),
    path('update_student/<int:pk>',views.update_student,name='update_student'),

]
