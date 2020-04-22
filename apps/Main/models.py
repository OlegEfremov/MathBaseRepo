import json

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from mptt.models import MPTTModel, TreeForeignKey

from apps.Main.constants import MATH_TYPE


class MathAttribute_Folder(MPTTModel):

    name = models.CharField(max_length=1000, default='DEFAULT')
    parent = TreeForeignKey('self', related_name='subfolders', on_delete=models.CASCADE, blank=True, null=True)
    system_name = models.CharField(max_length=1000, default='DEFAULT')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class MathAttribute(models.Model):

    name = models.CharField(max_length=1000, default='DEFAULT_MATHATTRIBUTE_NAME')
    # mathtype = models.CharField(choices=MATH_TYPE, max_length=1000, blank=True)
    folders = models.ManyToManyField(MathAttribute_Folder, related_name='mathattributes')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class SavedFilter_Folder(MPTTModel):

    name = models.CharField(max_length=1000, default='DEFAULT')
    parent = TreeForeignKey('self', related_name='subfolders', on_delete=models.CASCADE, blank=True, null=True)
    system_name = models.CharField(max_length=1000, default='DEFAULT')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class SavedFilter(models.Model):

    name = models.CharField(max_length=1000, default='DEFAULT_SAVEDFILTER_NAME')
    body = models.TextField(blank=True)
    folder = models.ForeignKey(SavedFilter_Folder, related_name='savedfilters', blank=True, on_delete=models.CASCADE, null=True, db_index=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='users', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Source_Folder(MPTTModel):

    name = models.CharField(max_length=1000, default='DEFAULT')
    parent = TreeForeignKey('self', related_name='subfolders', on_delete=models.CASCADE, blank=True, null=True)
    system_name = models.CharField(max_length=1000, default='DEFAULT')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Source(models.Model):

    name = models.CharField(max_length=1000, default='DEFAULT')
    info = models.TextField(blank=True, null=True)
    folders = models.ManyToManyField(Source_Folder, related_name='sources', blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Chapter(MPTTModel):

    name = models.CharField(max_length=1000, default='DEFAULT')
    parent = TreeForeignKey('self', related_name='subchapters', on_delete=models.CASCADE, blank=True, null=True)
    order = models.CharField(max_length=1000, blank=True, null=True, default='000000')
    source = models.ForeignKey(Source, on_delete=models.CASCADE, related_name='chapters', blank=True, null=True)
    system_name = models.CharField(max_length=1000, default='DEFAULT')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class TaskNumber(models.Model):

    body = models.CharField(max_length=1000)
    order = models.CharField(max_length=1000, blank=True, null=True, default='0')
    source = models.ForeignKey(Source, on_delete=models.CASCADE, related_name='tasknumbers')
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name='tasknumbers', blank=True, default=None, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.source.name +', ' + str(self.body)


class Task(models.Model):

    body = models.TextField()
    ans = models.TextField(blank=True)
    taskNumber = models.ManyToManyField(TaskNumber, related_name='tasks', blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.TextField(blank=True, default='')
    pic_task = models.FileField(blank=True)
    mpfile_task = models.FileField(blank=True)
    pic1 = models.ImageField(blank=True)
    pic2 = models.FileField(blank=True)
    mpfile1 = models.FileField(blank=True)
    mpfile2 = models.FileField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(self.id)


class Solution(models.Model):

    name = models.CharField(max_length=1000, default='DEFAULT_SOLUTION_NAME')
    body = models.TextField(blank=True)
    comment = models.TextField(blank=True, default='')
    instruction = models.TextField(default='', blank=True)
    mathAttribute = models.ManyToManyField(MathAttribute, related_name='solutions', blank=True)
    task = models.ForeignKey(Task, related_name='solutions', blank=True, on_delete=models.CASCADE,
                             null=True, db_index=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pic_sol = models.FileField(blank=True)
    mpfile_sol = models.FileField(blank=True)

    pic1 = models.FileField(blank=True)
    mpfile1 = models.FileField(blank=True)
    pic2 = models.FileField(blank=True)
    mpfile2 = models.FileField(blank=True)
    pic3 = models.FileField(blank=True)
    mpfile3 = models.FileField(blank=True)
    pic4 = models.FileField(blank=True)
    mpfile4 = models.FileField(blank=True)
    pic5 = models.FileField(blank=True)
    mpfile5 = models.FileField(blank=True)
    pic6 = models.FileField(blank=True)
    mpfile6 = models.FileField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(self.id)


class Solution_Folder(MPTTModel):

    name = models.CharField(max_length=1000, default='DEFAULT_FOLDER_NAME')
    system_name = models.CharField(max_length=1000, default='DEFAULT_FOLDER_SYSTEM_NAME')
    parent = TreeForeignKey('self', related_name='subfolders', on_delete=models.CASCADE, blank=True, null=True)
    solution = models.ManyToManyField(Solution, related_name='solution_folders', blank=True)
    tasks_order = models.TextField(default='{}', blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    access = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Test_Template(models.Model):

    name = models.CharField(max_length=1000, default='DEFAULT_TEST_TEMPLATE', verbose_name="Имя шаблона")
    comment = models.TextField(default='', blank=True, verbose_name="Комментарий")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    folders_and_numbers = models.TextField(default='', blank=True, verbose_name="Папки и номера задач")
    is_permanent = models.BooleanField(default=True, verbose_name="Постоянно")
    is_archived = models.BooleanField(default=False)

    def __str__(self):
        return self.name + ' id-' + str(self.id)


class Test_Generated(models.Model):

    name = models.CharField(max_length=1000, default='DEFAULT_TEST_NAME')
    comment = models.TextField(default='', blank=True)
    task = models.ManyToManyField(Task, related_name='test_generateds', blank=True)
    tasks_order = models.TextField(default='', blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    access = models.BooleanField(default = True)
    open_answers = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    template = models.ForeignKey(Test_Template, related_name='test_generateds', blank=True, on_delete=models.SET_NULL,
                             null=True, db_index=True, default=None)
    is_archived = models.BooleanField(default=False)

    def __str__(self):
        return self.name + ' id-' + str(self.id)


class Test_Folder(MPTTModel):

    name = models.CharField(max_length=1000, default='DEFAULT_FOLDER_NAME')
    system_name = models.CharField(max_length=1000, default='DEFAULT_FOLDER_SYSTEM_NAME')
    parent = TreeForeignKey('self', related_name='subfolders', on_delete=models.CASCADE, blank=True, null=True)
    test = models.ManyToManyField(Test_Generated, related_name='test_folders', blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def add_test(self, test_id):
        if type(test_id) == str:
            test = Test_Generated.objects.get(id=test_id)
            self.test.add(test)
        else:
            self.test.add(test_id)

    def remove_test(self, test_id):
        pass

    def rename(self, newname):
        pass

    def change_parent(self, new_parent):
        pass


class Star_Folder(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=False)
    checkbox_values = models.TextField(default=json.dumps({}), blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_checkbox_values(self):
        return json.loads(self.checkbox_values)

    def get_solutions(self):

        checkbox_values = self.get_checkbox_values()
        list_of_tasks_id = []
        list_of_sols_id = []
        for key, value in checkbox_values.items():
            if value:
                if 'task' in key:
                    list_of_tasks_id.append(key.replace('checkbox_task_', ''))
                if 'sol' in key:
                    list_of_sols_id.append(key.replace('checkbox_sol_', ''))

        solutions_set = Solution.objects.filter(id__in=list_of_sols_id)
        return solutions_set


    def get_tasks(self):
        checkbox_values = self.get_checkbox_values()
        list_of_tasks_id = []
        list_of_sols_id = []
        for key, value in checkbox_values.items():
            if value:
                if 'task' in key:
                    list_of_tasks_id.append(key.replace('checkbox_task_', ''))
                if 'sol' in key:
                    list_of_sols_id.append(key.replace('checkbox_sol_', ''))

        solutions_set = Solution.objects.filter(id__in=list_of_sols_id)

        tasks = Task.objects.filter(solutions__in=solutions_set).distinct()
        another_tasks = Task.objects.filter(id__in=list_of_tasks_id)

        tasks = set(tasks) | set(another_tasks)

        return tasks


# Загружаемые рисунки условий задач
class UploadedTaskImages(models.Model):

    task = models.ForeignKey(Task, on_delete=models.PROTECT)
    image = models.ImageField(upload_to='task_images/%Y/%m/%d/')
    name = models.CharField(max_length=200, blank=False)


# Загружаемые рисунки решений
class UploadedSolImages(models.Model):

    solution = models.ForeignKey(Solution, on_delete=models.PROTECT)
    image = models.ImageField(upload_to='sol_images/%Y/%m/%d/')
    name = models.CharField(max_length=200, blank=False)


