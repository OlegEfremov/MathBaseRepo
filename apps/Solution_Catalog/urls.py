from django.urls import re_path

from apps.Full_Search.views import attr_tree
from apps.Solution_Catalog.views import get_main_tree, get_user_tree, \
    rename_solution_folder, delete_solution_folder, copy_solution_folder, \
    move_solution_folder, create_solution_folder, copy_move_remove_task_or_solution, \
    main_page, show_tasks, show_tasks_without_solution, create_solution_for_empty_tasks, \
    show_tasks_outside_folders, reorder_tasks, export_folder, download_dynamic_text, create_task_in_folder,\
    view_folder_as_test, change_folder_access_status

urlpatterns = [
    re_path(r'main_page', main_page),
    re_path(r'attr_tree$', attr_tree),

    re_path(r'get_main_tree', get_main_tree),
    re_path(r'get_user_tree', get_user_tree),

    re_path(r'show_tasks$', show_tasks),
    re_path(r'show_tasks_without_solution', show_tasks_without_solution),
    re_path(r'create_solution_for_empty_tasks', create_solution_for_empty_tasks),
    re_path(r'show_tasks_outside_folders', show_tasks_outside_folders),


    re_path(r'copy_move_remove_task_or_solution', copy_move_remove_task_or_solution),

    re_path(r'create_solution_folder', create_solution_folder),
    re_path(r'rename_solution_folder', rename_solution_folder),
    re_path(r'delete_solution_folder', delete_solution_folder),
    re_path(r'move_solution_folder', move_solution_folder),
    re_path(r'copy_solution_folder', copy_solution_folder),

    re_path(r'reoder_tasks', reorder_tasks),

    re_path(r'export_folder_(?P<folder_id>\d+)', export_folder),
    re_path(r'download_dynamic_text', download_dynamic_text),
    re_path(r'create_task_in_folder', create_task_in_folder),

    re_path(r'test_(?P<folder_id>\d+)', view_folder_as_test),
    re_path(r'change_folder_access_status', change_folder_access_status),


]
