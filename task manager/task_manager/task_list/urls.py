from django.urls import path
from .views import *


urlpatterns = [
    path('<int:pk>/', DetailTask.as_view(),name='details_task'),
    # path('', ListTask.as_view(),name='list_task'),
    path('create/', CreateTask.as_view(),name='create_task'),  # Added a trailing slash for consistency
    path('delete/<int:pk>/', DeleteTask.as_view(),name='delete_task'),  # Added a trailing slash for consistency
    path('', TaskListView.as_view(),name='task_list'),
]
