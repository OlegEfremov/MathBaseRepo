from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from apps.Main.constants import path
from apps.Main.lib import get_current_user
from apps.Main.models import Source, Test_Generated


def main_page(request):
    sources = Source.objects.all()
    return render(request, 'All_Search/main_page.html', {'path': path, 'sources': sources})


def find_test_by_name(request):
    name = request.POST.get('test_name')

    tests = Test_Generated.objects.filter(author=get_current_user(request)).filter(name__icontains=name)


    return render(request, 'All_Search/test_links.html', {'path': path, 'tests': tests})