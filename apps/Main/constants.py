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

# This arrays need for filterQuerry
NODE_MATH_TYPE = ['MathAttr']
NODE_MATH_TYPE_EXCLUDE = ['EXCLUDE_MathAttr']

# пароль для вызова страницы списка задач избранного
PASS_PDF = "Rtb90.DFg56901qFG"
# список id галочек на странице избранного передаваемые как параметр в страницу списка задач
LIST_CHECKBOXES = ('id_number', 'task_body', 'sources', 'answer', 'solutions', 'another_solutions', 'mathattr', 'ans_table')
