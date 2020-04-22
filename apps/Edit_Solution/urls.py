from django.urls import re_path

from apps.Edit_Solution.views import main_page, mathattr_tree, solattr_tree, delete_mathattribue_from_solution, \
    add_attr_to_sol, delete_solution, show_tasks, save_solution

from apps.Edit_MathAttribute_Catalog.views import rename_node, copy_node, move_node, create_node, delete_node_from_db, remove_node_from_folder, \
    create_mathattr_folder, create_mathattr
from apps.Main.views import sol_image_upload

urlpatterns = [
    re_path(r'main_page_(?P<sol_id>\d+)', main_page, name="sol_main_page"),

    re_path(r'mathattr_tree', mathattr_tree),
    re_path(r'solattr_tree/(?P<sol_id>\d+)', solattr_tree),
    re_path(r'delete_mathattribue_from_solution', delete_mathattribue_from_solution),
    re_path(r'add_attr_to_sol', add_attr_to_sol),
    re_path(r'delete_solution_(?P<sol_id>\d+)', delete_solution),
    re_path(r'show_tasks', show_tasks),
    re_path(r'save_solution', save_solution),

    re_path(r'rename_node', rename_node),
    re_path(r'copy_node', copy_node),
    re_path(r'^move_node$', move_node),
    re_path(r'create_node', create_node),
    re_path(r'delete_node_from_db', delete_node_from_db),
    re_path(r'remove_node_from_folder', remove_node_from_folder),
    re_path(r'create_mathattr_folder', create_mathattr_folder),
    re_path(r'create_mathattr', create_mathattr),
    re_path(r'sol_image_upload_(?P<sol_id>\d+)', sol_image_upload, name="sol_image_upload"),

]

