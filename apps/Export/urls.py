from django.urls import re_path

from apps.Export.views import main_page, main_page_system, show_tasks_cart
from apps.Full_Search.views import attr_tree
from apps.Main.views import get_list_of_sols_id_in_task
from apps.Solution_Catalog.views import get_user_tree, copy_move_remove_task_or_solution, create_solution_folder, \
    rename_solution_folder, get_main_tree

urlpatterns = [
    re_path(r'main_page_system', main_page_system),
    re_path(r'main_page', main_page),
    re_path(r'show_tasks_cart', show_tasks_cart),
    re_path(r'get_user_tree', get_user_tree),
    re_path(r'get_main_tree', get_main_tree),
    re_path(r'copy_move_remove_task_or_solution', copy_move_remove_task_or_solution),

    re_path(r'create_solution_folder', create_solution_folder),
    re_path(r'rename_solution_folder', rename_solution_folder),

    re_path(r'attr_tree$', attr_tree),
    re_path(r'get_list_of_sols_id_in_task', get_list_of_sols_id_in_task),
]
