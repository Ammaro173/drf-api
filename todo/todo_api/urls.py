from django.urls import re_path as url
from django.urls import path, include
from .views import (
    TodoListApiView,
)
from todo_api.api.viewset import (
    TodoDetailApiView,
)

urlpatterns = [
    path("api/list", TodoListApiView.as_view(), name="todo_list"),
    path("api/<int:todo_id>", TodoDetailApiView.as_view(), name="todo_detail"),
]
