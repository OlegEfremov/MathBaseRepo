from django.urls import re_path

from apps.Edit_Source_Catalog.views import rename_node, copy_node, move_node, \
    delete_node_from_db, remove_node_from_folder, create_source_folder, create_source, create_task_number, \
    create_task, create_chapter

from apps.Edit_Task.views import main_page, source_tree, tasksource_tree, delete_tasknumber_from_task, \
    add_task_number_to_task, deletetask, show_tasks, save_task, create_new_solution, delete_solution, \
    source_folder_node_tree, source_node_tree, chapter_node_tree
from apps.Main.views import task_image_upload, sol_image_upload

urlpatterns = [
    # re_path(r'main_page', main_page),
    re_path(r'main_page_(?P<task_id>\d+)', main_page, name="task_main_page"),
    re_path(r'tasksource_tree/(?P<task_id>\d+)', tasksource_tree),

    re_path(r'source_tree/Source_Folder/(?P<dbID>\d+)', source_folder_node_tree),
    re_path(r'source_tree/Source/(?P<dbID>\d+)', source_node_tree),
    re_path(r'source_tree/Chapter/(?P<dbID>\d+)', chapter_node_tree),
    re_path(r'source_tree$', source_tree),

    re_path(r'delete_tasknumber_from_task', delete_tasknumber_from_task),
    re_path(r'add_task_number_to_task', add_task_number_to_task),

    re_path(r'deletetask/(?P<task_id>\d+)', deletetask),
    re_path(r'show_tasks', show_tasks),
    re_path(r'save_task', save_task),
    re_path(r'create_new_solution', create_new_solution),
    re_path(r'delete_solution', delete_solution),

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
    re_path(r'task_image_upload_(?P<task_id>\d+)', task_image_upload, name="task_image_upload"),
]
