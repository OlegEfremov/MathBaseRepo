from django.urls import re_path

from apps.BelovedCat.views import main_page, qsto, qstot, qstott, qstottr, qstottry, qstottryed

urlpatterns = [

    re_path(r'main_page', main_page),
    re_path(r'qstottryed', qstottryed),
    re_path(r'qstottry', qstottry),
    re_path(r'qstottr', qstottr),
    re_path(r'qstott', qstott),
    re_path(r'qstot', qstot),
    re_path(r'qsto', qsto),
]
