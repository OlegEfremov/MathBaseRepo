from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from apps.Main.models import MathAttribute_Folder, MathAttribute, SavedFilter_Folder, SavedFilter, Solution, \
    Solution_Folder, Source, TaskNumber, Task, Source_Folder, Chapter, Test_Generated, Test_Template, Star_Folder, \
    Test_Folder
from apps.Main.resources import MathAttribute_FolderAdmin, SavedFilter_FolderAdmin, Solution_FolderAdmin, \
    Source_FolderAdmin, TaskResource, SolutionResource, TaskNumberResource, ChapterAdmin, Test_FolderAdmin


class TaskNumberAdmin(ImportExportModelAdmin):
    resource_class = TaskNumberResource


class TaskAdmin(ImportExportModelAdmin):
    resource_class = TaskResource


class SolutionAdmin(ImportExportModelAdmin):
    resource_class = SolutionResource


admin.site.register(MathAttribute)
admin.site.register(MathAttribute_Folder, MathAttribute_FolderAdmin)

admin.site.register(SavedFilter)
admin.site.register(SavedFilter_Folder, SavedFilter_FolderAdmin)

admin.site.register(Solution, SolutionAdmin)
admin.site.register(Solution_Folder, Solution_FolderAdmin)

admin.site.register(Task, TaskAdmin)
admin.site.register(TaskNumber, TaskNumberAdmin)

admin.site.register(Source)
admin.site.register(Source_Folder, Source_FolderAdmin)
admin.site.register(Chapter, ChapterAdmin)
admin.site.register(Test_Generated)
admin.site.register(Test_Template)
admin.site.register(Star_Folder)
admin.site.register(Test_Folder, Test_FolderAdmin)


