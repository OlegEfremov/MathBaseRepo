from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from apps.BelovedCat.forms import CatForm
from apps.Main.constants import path


def qstottryed(request):
    catform = CatForm(request.POST or None)
    catform.is_valid()
    answer = ''
    if (catform.is_valid()):
        answer = catform.cleaned_data.get('answer')

    if answer == '':
        return render(request, 'BelovedCat/main_page.html', {'path': path, 'catform': catform, 'question': 'Заяц', 'text': 'Что ответишь?'})
    elif answer == '' or answer == '':
        return render(request, 'BelovedCat/final.html', {'path': path})
    else:
        return render(request, 'BelovedCat/main_page.html',
                      {'path': path, 'catform': catform,  'question': 'Котей...', 'text': 'Похоже, ты не настоящий кот.'})
    return HttpResponse('{}')


def qstottry(request):
    catform = CatForm(request.POST or None)
    catform.is_valid()
    answer = ''
    if (catform.is_valid()):
        answer = catform.cleaned_data.get('answer')

    if answer == '':
        return render(request, 'BelovedCat/main_page.html', {'path': path, 'catform': catform, 'question': 'Карась', 'text': 'Что ответишь?'})
    elif answer == '' or answer == '' or answer == '' or answer == '':
        return redirect(qstottryed)
    else:
        return render(request, 'BelovedCat/main_page.html',
                      {'path': path, 'catform': catform,  'question': 'Котей...', 'text': 'Похоже, ты не настоящий кот.'})
    return HttpResponse('{}')



def qstottr(request):
    catform = CatForm(request.POST or None)
    catform.is_valid()
    answer = ''
    if (catform.is_valid()):
        answer = catform.cleaned_data.get('answer')

    if answer == '':
        return render(request, 'BelovedCat/main_page.html', {'path': path, 'catform': catform, 'question': 'Кот', 'text': 'Что ответишь?'})
    elif answer == '' or answer == '' or answer == '' or answer == '':
        return redirect(qstottry)
    else:
        return render(request, 'BelovedCat/main_page.html',
                      {'path': path, 'catform': catform,  'question': 'Котей...', 'text': 'Похоже, ты не настоящий кот.'})
    return HttpResponse('{}')

def qstott(request):
    catform = CatForm(request.POST or None)
    catform.is_valid()
    answer = ''
    if (catform.is_valid()):
        answer = catform.cleaned_data.get('answer')

    if answer == '':
        return render(request, 'BelovedCat/main_page.html', {'path': path, 'catform': catform, 'question': 'Котей...', 'text': 'Что ответишь?'})
    elif answer == '' or answer == '' or answer == '' or answer == '':
        return redirect(qstottr)
    else:
        return render(request, 'BelovedCat/main_page.html',
                      {'path': path, 'catform': catform,  'question': 'Котей...', 'text': 'Похоже, ты не настоящий кот.'})
    return HttpResponse('{}')


def qstot(request):
    catform = CatForm(request.POST or None)
    catform.is_valid()
    answer = ''
    if (catform.is_valid()):
        answer = catform.cleaned_data.get('answer')

    if answer == '':
        return render(request, 'BelovedCat/main_page.html', {'path': path, 'catform': catform, 'question': 'День...', 'text': 'Что ответишь?'})
    elif answer == '' or answer == '' or answer == '' or answer == '':
        return redirect(qstott)
    else:
        return render(request, 'BelovedCat/main_page.html',
                      {'path': path, 'catform': catform,  'question': 'День...', 'text': 'Похоже, ты не настоящий кот.'})
    return HttpResponse('{}')

def qsto(request):
    catform = CatForm(request.POST or None)
    catform.is_valid()
    answer = ''
    if (catform.is_valid()):
        answer = catform.cleaned_data.get('answer')

    if answer == '':
        return render(request, 'BelovedCat/main_page.html', {'path': path, 'catform': catform, 'question': 'Смотреть что?', 'text': 'Что ответишь?'})
    elif answer == '' or answer == '':
        return redirect(qstot)
    else:
        return render(request, 'BelovedCat/main_page.html',
                      {'path': path, 'catform': catform,  'question': 'Смотреть что?', 'text': 'Похоже, ты не настоящий кот.'})
    return HttpResponse('{}')


def main_page(request):

    catform = CatForm(request.POST or None)
    catform.is_valid()
    answer = ''
    if (catform.is_valid()):
        answer = catform.cleaned_data.get('answer')

    if answer == '':
        return render(request, 'BelovedCat/main_page.html', {'path': path, 'catform': catform,  'question': 'Ты точно кот?', 'text': 'Что ответишь?'})
    elif answer == '' or answer == '':
        return redirect(qsto)
    else:
        return render(request, 'BelovedCat/main_page.html', {'path': path, 'catform': catform,  'question': 'Ты точно кот?', 'text': 'Похоже, ты не настоящий кот.'})


