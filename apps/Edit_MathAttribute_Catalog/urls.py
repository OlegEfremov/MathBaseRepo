from django.urls import re_path

from apps.Edit_MathAttribute_Catalog.views import main_page, edit_mathattr_tree, \
    rename_node, copy_node, move_node, create_node, delete_node_from_db, remove_node_from_folder, \
    create_mathattr_folder, create_mathattr

urlpatterns = [

    re_path(r'main_page', main_page),
    re_path(r'edit_mathattr_tree', edit_mathattr_tree),

    re_path(r'rename_node', rename_node),
    re_path(r'copy_node', copy_node),
    re_path(r'^move_node$', move_node),
    re_path(r'create_node', create_node),
    re_path(r'delete_node_from_db', delete_node_from_db),
    re_path(r'remove_node_from_folder', remove_node_from_folder),
    re_path(r'create_mathattr_folder', create_mathattr_folder),
    re_path(r'create_mathattr', create_mathattr),
]
