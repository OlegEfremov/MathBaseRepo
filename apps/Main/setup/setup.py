from apps.Main.models import MathAttribute_Folder

FOLDER_MATH_TYPE = (
    ('OBJECTS', 'Объекты'),
    ('FACTS', 'Факты'),
    ('FEATURES', 'Особенности'),
    ('TASKTYPES', 'Типы задач'),
    ('METHODS', 'Методы'),
    ('ALL_MATHATTRIBUTES', 'Все атрибуты'),
)


def setup():
    root = MathAttribute_Folder(name='Дерево всех атрибутов', system_name='ROOT_MATHATTRIBUTES').save()
    for i in range(len(FOLDER_MATH_TYPE)):
        MathAttribute_Folder(name=FOLDER_MATH_TYPE[i][1], system_name=FOLDER_MATH_TYPE[i][0], parent = root).save()
