from django.urls import re_path


from apps.Full_Search.views import user_main_page, sys_main_page, attr_tree, show_tasks, get_json_all_mathattr_in_filter, find_task_by_id
from apps.Solution_Catalog.views import get_user_tree, copy_move_remove_task_or_solution, create_solution_folder, \
    rename_solution_folder, get_main_tree

urlpatterns = [
    re_path(r'user/main_page', user_main_page),
    re_path(r'system/main_page', sys_main_page),
    re_path(r'attr_tree$', attr_tree),
    re_path(r'show_tasks', show_tasks),
    re_path(r'find_task_by_id', find_task_by_id),
    re_path(r'get_user_tree', get_user_tree),
    re_path(r'get_main_tree', get_main_tree),

    re_path(r'get_json_all_mathattr_in_filter', get_json_all_mathattr_in_filter),

    re_path(r'copy_move_remove_task_or_solution', copy_move_remove_task_or_solution),

    re_path(r'create_solution_folder', create_solution_folder),
    re_path(r'rename_solution_folder', rename_solution_folder),

]
