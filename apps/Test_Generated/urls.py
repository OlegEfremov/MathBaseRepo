from django.urls import re_path, path

from apps.Solution_Catalog.views import get_user_tree
from apps.Test_Generated.views import view_test, test_from_many_folders, create_test_from_many_folders, make_new_test, \
    created_tests, create_test_from_cart, create_test_template, create_test_by_template, save_test_name_and_comment, \
    recompile_test, archive_test, random_change_task_in_test, open_test_answers, TestTemplateUpdateView, \
    delete_template_task

urlpatterns = [
    re_path(r'template_update_(?P<pk>\d+)', TestTemplateUpdateView.as_view(), name='template_update'),
    re_path(r'delete_template_task_(?P<pk>\d+)', delete_template_task, name='template_delete'),
    re_path(r'(?P<test_id>\d+)', view_test),
    re_path(r'recompile_test', recompile_test),
    re_path(r'create_test_from_many_folders', create_test_from_many_folders),
    re_path(r'test_from_many_folders', test_from_many_folders, name='test_from_many_folders'),
    re_path(r'get_user_tree', get_user_tree),
    re_path(r'make_new_test', make_new_test),
    re_path(r'created_tests', created_tests),
    re_path(r'create_test_from_cart', create_test_from_cart),
    re_path(r'create_test_template', create_test_template),
    re_path(r'create_test_by_template', create_test_by_template),
    re_path(r'save_test_name_and_comment', save_test_name_and_comment),
    re_path(r'archive_test', archive_test),
    re_path(r'random_change_task_in_test', random_change_task_in_test),
    re_path(r'open_test_answers', open_test_answers),
]
