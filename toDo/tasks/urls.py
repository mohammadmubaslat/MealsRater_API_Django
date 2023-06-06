from django.urls import path
from .views import GetTasks, SingleTask, AddTask, UpdateTask

urlpatterns = [
    path("", GetTasks.as_view(), name='get_all'),
    path('<int:pk>', SingleTask.as_view(), name='get_single_task'),
    path('task', AddTask.as_view(), name='add_task'),
    path('update/<int:pk>', UpdateTask.as_view(), name='update'),
]
