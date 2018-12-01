from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addTodo', views.addTodo, name='add'),
    path('complete/<todo_id>', views.completedTodo, name='completedTodo'),
    path('deletecompleted/', views.deleteCompleted, name='deleteCompleted'),
    path('deleteall/', views.deleteAll, name='deleteAll'),

]
