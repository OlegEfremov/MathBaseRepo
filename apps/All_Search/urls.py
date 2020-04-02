from django.urls import re_path

from apps.All_Search.views import main_page, find_test_by_name
from apps.Edit_Source_Catalog.views import find_task_by_source_and_number
from apps.Full_Search.views import find_task_by_id

urlpatterns = [
    re_path(r'main_page', main_page),
    re_path(r'find_task_by_id', find_task_by_id),
    re_path(r'find_task_by_source_and_number', find_task_by_source_and_number),
    re_path(r'find_test_by_name', find_test_by_name),
]

