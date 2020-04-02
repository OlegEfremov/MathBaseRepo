import json

from django.http import HttpResponse, JsonResponse

from apps.Main.lib import get_current_user
from apps.Main.views import get_or_create_star_folder
from apps.crm_actions.views import get_tasks_and_sols_from_values_list


def squares_to_stars(request):
    square_values = json.loads(request.POST.get('square_values'))

    user = get_current_user(request)
    if user.is_authenticated:
        star_folder = get_or_create_star_folder(user)
        checkbox_values = json.loads(star_folder.checkbox_values)

        for key, value in square_values.items():
            if value:
                checkbox_values[key.replace('squares', 'checkbox')] = True

        user.star_folder.checkbox_values = checkbox_values
        user.star_folder.save()
    return HttpResponse('{}')