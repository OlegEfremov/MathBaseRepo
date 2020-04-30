from django.contrib.auth.models import User, AnonymousUser


def get_current_user(request):
    if request.user.is_authenticated:
        user_id = request.user.id
        current_user = User.objects.get(id=user_id)
    else:
        current_user = AnonymousUser()
    return current_user


# берет id пользователя из GET параметра
def get_user_param(request):
    if request.user.is_authenticated:
        user_id = request.user.id
        current_user = User.objects.get(id=user_id)
    else:
        user_id = int(request.GET.get("id", 0))
        if user_id > 0:
            current_user = User.objects.get(id=user_id)
        else:
            current_user = AnonymousUser()

    return current_user
