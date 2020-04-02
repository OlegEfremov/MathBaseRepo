from django.urls import re_path

from apps.Main.py.Test_Folder.test_folder_tree import get_test_folder_tree, test_folder_new_child_chapter, \
    rename_test_folder, copy_test_folder, move_test_folder, delete_test_folder_from_db, show_tests_in_folder, \
    show_all_user_tests, move_test_to_another_folder, show_user_tests_outside_folders

urlpatterns = [
    re_path(r'get_test_folder_tree', get_test_folder_tree),
    re_path(r'test_folder_new_child_chapter', test_folder_new_child_chapter),
    re_path(r'rename_test_folder', rename_test_folder),
    re_path(r'copy_test_folder', copy_test_folder),
    re_path(r'move_test_folder', move_test_folder),
    re_path(r'delete_test_folder_from_db', delete_test_folder_from_db),

    re_path(r'show_tests_in_folder', show_tests_in_folder),
    re_path(r'show_all_user_tests', show_all_user_tests),
    re_path(r'move_test_to_another_folder', move_test_to_another_folder),
    re_path(r'show_user_tests_outside_folders', show_user_tests_outside_folders),
]

