from django.urls import re_path

from apps.Edit_Source_Catalog.views import main_page, rename_node, copy_node, move_node, \
    delete_node_from_db, remove_node_from_folder, create_source_folder, create_source, create_task_number, \
    show_tasks, create_task, create_chapter, import_tasks, export_tasknumbers_csv, export_tasks_csv, \
    find_task_by_source_and_number, edit_and_import, test_csv

from apps.Edit_Task.views import source_tree, source_node_tree, chapter_node_tree, source_folder_node_tree
from apps.Solution_Catalog.views import get_main_tree, get_user_tree, copy_move_remove_task_or_solution, \
    create_solution_folder, rename_solution_folder, delete_solution_folder, move_solution_folder, copy_solution_folder





urlpatterns = [

    re_path(r'main_page_system', main_page),
    re_path(r'main_page', main_page),

    re_path(r'source_tree/Source_Folder/(?P<dbID>\d+)', source_folder_node_tree),
    re_path(r'source_tree/Source/(?P<dbID>\d+)', source_node_tree),
    re_path(r'source_tree/Chapter/(?P<dbID>\d+)', chapter_node_tree),
    re_path(r'source_tree$', source_tree),

    re_path(r'rename_node', rename_node),
    re_path(r'copy_node', copy_node),
    re_path(r'^move_node$', move_node),
    re_path(r'create_source_folder', create_source_folder),
    re_path(r'^create_source$', create_source),
    re_path(r'create_task_number', create_task_number),

    re_path(r'create_task', create_task),
    re_path(r'create_chapter', create_chapter),

    re_path(r'delete_node_from_db', delete_node_from_db),
    re_path(r'remove_node_from_folder', remove_node_from_folder),

    re_path(r'show_tasks', show_tasks),

    re_path(r'get_main_tree', get_main_tree),
    re_path(r'get_user_tree', get_user_tree),

    re_path(r'copy_move_remove_task_or_solution', copy_move_remove_task_or_solution),
    re_path(r'create_solution_folder', create_solution_folder),
    re_path(r'rename_solution_folder', rename_solution_folder),
    re_path(r'delete_solution_folder', delete_solution_folder),
    re_path(r'move_solution_folder', move_solution_folder),
    re_path(r'copy_solution_folder', copy_solution_folder),

    re_path(r'import_tasks', import_tasks),
    re_path(r'export_tasks_csv', export_tasks_csv),
    re_path(r'export_tasknumbers_csv', export_tasknumbers_csv),
    re_path(r'find_task_by_source_and_number', find_task_by_source_and_number),

    re_path(r'edit_and_import', edit_and_import),
    re_path(r'test_csv', test_csv),

]
