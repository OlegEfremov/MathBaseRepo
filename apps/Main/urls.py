from django.urls import re_path

from apps.Main.views import main_page, export_as_file

urlpatterns = [
    re_path(r'export_as_file', export_as_file),
    re_path(r'main_page', main_page),
    re_path(r'', main_page),
]
