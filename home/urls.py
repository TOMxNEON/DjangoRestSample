from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('post_task',post_task, name="post_task"),
    path('get_tasks',get_tasks,name= "get_tasks"),
    path('update_task',patch_task,name="update_task"),
]
