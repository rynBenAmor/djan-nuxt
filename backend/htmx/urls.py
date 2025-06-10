# tasks_htmx/urls.py

from django.urls import path
from . import views

app_name = 'htmx'

urlpatterns = [
    path('', views.index, name='index'),
    
    path('task-list/', views.task_list, name='task_list'),
    path("add/", views.add_task, name="add_task"),
    path("toggle/<int:pk>/", views.toggle_task, name="toggle_task"),
    path("delete/<int:pk>/", views.delete_task, name="delete_task"),

    path('public-record/', views.get_PR, name='get_pr'),
    path('hello-world', views.hello_world, name='greetings'),
    path('htmx/toggle-message/', views.toggle_message, name='toggle_message'),

    path('message/list/', views.message_list, name='message_list'),
    path('message/add/', views.message_add, name='message_add'),

    path('post/list/', views.post_list, name='post_list'),
    path('post/like/<int:post_id>/', views.post_like, name='post_like'),
    path('post/search/', views.post_search, name='post_search'),
    path('post/create/', views.post_create, name='post_create'),

]
