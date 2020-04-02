from django.urls import re_path

from apps.crm_actions.add_attribute_massive import add_attribute_massive
from apps.crm_actions.squares_to_stars import squares_to_stars
from apps.crm_actions.views import copy_massive, erase_massive, move_massive

urlpatterns = [
    re_path(r'copy_massive', copy_massive),
    re_path(r'move_massive', move_massive),
    re_path(r'erase_massive', erase_massive),
    re_path(r'squares_to_stars', squares_to_stars),
    re_path(r'add_attribute_massive', add_attribute_massive),
]
