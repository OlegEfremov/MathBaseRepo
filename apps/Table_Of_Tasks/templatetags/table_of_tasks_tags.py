from django import template
from django.contrib.auth.models import Group
# from django.contrib.sites.models import Site

register = template.Library()

# @register.simple_tag
# def current_domain():
#     return 'http://%s' % Site.objects.get_current().domain

@register.filter(name='has_another_sols')
def has_another_sols(task_solutions, sols):
    # set = task_solutions.exclude(sols)
    a = set(task_solutions)-set(sols)
    return False if a == set() else True

@register.filter(name='has_group')
def has_group(user, group_name):
    group = Group.objects.get(name=group_name)
    return True if group in user.groups.all() else False


class SetVarNode(template.Node):
    def __init__(self, new_val, var_name):
        self.new_val = new_val
        self.var_name = var_name
    def render(self, context):
        context[self.var_name] = self.new_val
        return ''

import re
@register.tag
def setvar(parser,token):
    tag_name, arg = token.contents.split(None, 1)

    m = re.search(r'(.*?) as (\w+)', arg)
    new_val, var_name = m.groups()
    return SetVarNode(new_val[1:-1], var_name)

