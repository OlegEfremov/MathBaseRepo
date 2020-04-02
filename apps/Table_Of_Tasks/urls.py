from django.urls import re_path

from apps.Table_Of_Tasks.views import get_table_of_tasks

urlpatterns = [
    re_path(r'get_table_of_tasks', get_table_of_tasks),
]
