from django_mptt_admin.admin import DjangoMpttAdmin

from apps.Main.models import Task, TaskNumber, Solution

from import_export import fields, resources
from import_export.widgets import ManyToManyWidget



class MathAttribute_FolderAdmin(DjangoMpttAdmin):
    pass


class SavedFilter_FolderAdmin(DjangoMpttAdmin):
    pass


class Solution_FolderAdmin(DjangoMpttAdmin):
    pass


class Test_FolderAdmin(DjangoMpttAdmin):
    pass


class Source_FolderAdmin(DjangoMpttAdmin):
    pass


class ChapterAdmin(DjangoMpttAdmin):
    pass


class TaskResource(resources.ModelResource):

    class Meta:
        model = Task


class TaskNumberResource(resources.ModelResource):

    class Meta:
        model = TaskNumber


class SolutionResource(resources.ModelResource):
    class Meta:
        model = Solution

