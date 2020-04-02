# Установить mysql, создать юзера leobreslav и базу lbbase_db


# Все приложения должны быть расположены в папке apps
# В файлах apps/%Apps%/apps.py:
#      изменить name = 'apps.%AppName%'

# Заменить файлы в virtual environment на файлы из каталога to_copy (убрать из имён суффикс .to_copy)
#       \venv\Lib\site-packages\import_export\fields.py
#       \venv\Lib\site-packages\import_export\resources.py
# В файле
#       C:\MyProject\LBBase_v_0_36\venv\Lib\site-packages\tablib\formats\_csv.py
#       Заменить DEFAULT_DELIMITER = '@'

# В файле settings.py:
#      INSTALLED_APPS = [
#          'mptt',
#          'django_mptt_admin',
#          'import_export',
#          'apps.MyApp.apps.MyappConfig',...]

# Запустить makemigrations+migrate

# makemigrations+migrate
# Создать superuser'а c логином и паролем:
#       createsuperuser
#         leobreslav
#         amtro915

# Через админку создать группы Admins, Editors, Readers, Superusers и по одному пользователю в каждой


from apps.Folder.models import Folder

# переменная path используется для путей к статике и для ссылок в url'aх
path = {
        'PROJECT_STATIC': '../../static/',
        'PROJECT_ROOT': '../../'
    }

# MATH_TYPE используется в поле mathtype модели Edit_MathAttribute_Catalog
# На первой позиции внутренне имя, на второй позиции -- имя, показываемое пользователю

MATH_TYPE = (
    ('Object', 'Объект'),
    ('Fact', 'Факт'),
    ('Feature', 'Особенность'),
    ('TaskType', 'Тип задачи'),
    ('Method', 'Метод')
)

# Типы вершин для jstree - используются в apps.AdvSearch.lib.filterQuery
# Эти массивы должны быть согласованы с инициализацией деревьев в apps\AdvSearch\static\AdvSearch\js\advsearch_tree.js
NODE_MATH_TYPE = ['FILTER_leaf', 'Method', 'Fact', 'Feature', 'TaskType', 'Object']
NODE_MATH_TYPE_EXCLUDE = ['EXCLUDE_leaf', 'EXCLUDE_Method', 'EXCLUDE_Fact', 'EXCLUDE_Feature', 'EXCLUDE_TaskType', 'EXCLUDE_Object']


FOLDER_MATH_TYPE = (
    ('OBJECTS', 'Объекты'),
    ('FACTS', 'Факты'),
    ('FEATURES', 'Особенности'),
    ('TASKTYPES', 'Типы задач'),
    ('METHODS', 'Методы'),
    ('ALL_MATHATTRIBUTES', 'Все атрибуты'),
    ('ROOT_MATHATTRIBUTES', 'Дерево всех атрибутов')
)
def setup():
    for i in range(len(FOLDER_MATH_TYPE)):
        Folder(name=FOLDER_MATH_TYPE[i][1], system_name=FOLDER_MATH_TYPE[i][0]).save()
    Folder(name='Источники', system_name='ALL_SOURCES').save()
    Folder(name='Все решения', system_name='ALL_SOLUTIONS').save()
    Folder(name='Все условия', system_name='ALL_TASKS').save()
    Folder(name='Cохраненные поисковые запросы', system_name='SAVED_FILTERS').save()