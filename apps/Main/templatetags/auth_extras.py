from django import template
from django.contrib.auth.models import Group

register = template.Library()


@register.filter(name='has_group')
def has_group(user, group_name):
    group = Group.objects.get(name=group_name)
    return True if group in user.groups.all() else False


@register.filter(name='access_group')
def member_groups(user, group_name):
    if not user.is_authenticated:
        return False
    if user.is_superuser:
        return True
    if user.groups.filter(name__in=("Admins", "Superusers")).exists():
        return True

    if group_name == "Readers":
        return user.groups.filter(name__in=("Readers", "Editors", "Freinds")).exists()
    elif group_name == "Editors":
        return user.groups.filter(name="Editors").exists()
    elif group_name == "Freinds":
        return user.groups.filter(name="Freinds").exists()

    return False
