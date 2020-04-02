from django.urls import path, re_path

from apps.AdvSearch.views import advsearch, attr_tree, show_tasks, get_json_all_mathattr_in_filter, \
    show_tasks_without_solution, create_new_sol_for_empty_tasks
from apps.SavedFilter.views import save_filter_page

urlpatterns = [
    re_path(r'^$', advsearch, name='advsearch'),
    re_path(r'^attr_tree$', attr_tree, name='attr_tree'),
    re_path(r'show_tasks_without_solution', show_tasks_without_solution, name='show_tasks_without_solution'),
    re_path(r'show_tasks', show_tasks, name='show_tasks'),
    re_path(r'get_json_all_mathattr_in_filter', get_json_all_mathattr_in_filter, name='get_json_all_mathattr_in_filter'),
    re_path(r'create_new_sol_for_empty_tasks', create_new_sol_for_empty_tasks, name='create_new_sol_for_empty_tasks'),
    re_path(r'save_filter_page', save_filter_page, name=''),
]




# re_path(r'advsearch/attr_tree', attr_tree, name='attr_tree'),
# re_path(r'advsearch/current_filter', current_filter, name='current_filter'),
# re_path(r'advsearch/filter_tree', filter_tree, name='filter_tree'),
# re_path(r'advsearch/save_filter', save_filter, name='save_filter'),
# re_path(r'advsearch/disabled_drop_savedfilter', disabled_drop_savedfilter, name='disabled_drop_savedfilter'),
# re_path(r'advsearch/disabled_folderdrop_savedfilter', disabled_folderdrop_savedfilter,
#         name='disabled_folderdrop_savedfilter'),


# re_path(r'advsearch', advsearch, name='advsearch'),