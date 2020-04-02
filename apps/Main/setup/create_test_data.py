from apps.Main.models import MathAttribute_Folder, MathAttribute, Source, TaskNumber, Task, Solution, Source_Folder


# Функция создаёт минимальный набор тестовых данных в базе
# По два математических атрибута каждого типа и  шесть задач с решениями
def create_test_data():
    obj_attr1 = MathAttribute(name = 'Объект 1', mathtype='Object')
    obj_attr1.save()
    obj_folder = MathAttribute_Folder.objects.get(system_name='OBJECTS')
    allMA_folder = MathAttribute_Folder.objects.get(system_name='ALL_MATHATTRIBUTES')
    obj_attr1.folders.add(obj_folder)
    obj_attr1.folders.add(allMA_folder)


    obj_attr2 = MathAttribute(name = 'Объект 2', mathtype='Object')
    obj_attr2.save()
    obj_folder = MathAttribute_Folder.objects.get(system_name='OBJECTS')
    allMA_folder = MathAttribute_Folder.objects.get(system_name='ALL_MATHATTRIBUTES')
    obj_attr2.folders.add(obj_folder)
    obj_attr2.folders.add(allMA_folder)



    obj_attr3 = MathAttribute(name='Факт 1', mathtype='Fact')
    obj_attr3.save()
    obj_folder = MathAttribute_Folder.objects.get(system_name='FACTS')
    allMA_folder = MathAttribute_Folder.objects.get(system_name='ALL_MATHATTRIBUTES')
    obj_attr3.folders.add(obj_folder)
    obj_attr3.folders.add(allMA_folder)


    obj_attr4 = MathAttribute(name='Факт 2', mathtype='Fact')
    obj_attr4.save()
    obj_folder = MathAttribute_Folder.objects.get(system_name='FACTS')
    allMA_folder = MathAttribute_Folder.objects.get(system_name='ALL_MATHATTRIBUTES')
    obj_attr4.folders.add(obj_folder)
    obj_attr4.folders.add(allMA_folder)


    obj_attr5 = MathAttribute(name='Особенность 1', mathtype='Feature')
    obj_attr5.save()
    obj_folder = MathAttribute_Folder.objects.get(system_name='FEATURES')
    allMA_folder = MathAttribute_Folder.objects.get(system_name='ALL_MATHATTRIBUTES')
    obj_attr5.folders.add(obj_folder)
    obj_attr5.folders.add(allMA_folder)

    obj_attr6 = MathAttribute(name='Особенность 2', mathtype='Feature')
    obj_attr6.save()
    obj_folder = MathAttribute_Folder.objects.get(system_name='FEATURES')
    allMA_folder = MathAttribute_Folder.objects.get(system_name='ALL_MATHATTRIBUTES')
    obj_attr6.folders.add(obj_folder)
    obj_attr6.folders.add(allMA_folder)

    obj_attr7 = MathAttribute(name='Метод 1', mathtype='Method')
    obj_attr7.save()
    obj_folder = MathAttribute_Folder.objects.get(system_name='METHODS')
    allMA_folder = MathAttribute_Folder.objects.get(system_name='ALL_MATHATTRIBUTES')
    obj_attr7.folders.add(obj_folder)
    obj_attr7.folders.add(allMA_folder)

    obj_attr8 = MathAttribute(name='Метод 2', mathtype='Method')
    obj_attr8.save()
    obj_folder = MathAttribute_Folder.objects.get(system_name='METHODS')
    allMA_folder = MathAttribute_Folder.objects.get(system_name='ALL_MATHATTRIBUTES')
    obj_attr8.folders.add(obj_folder)
    obj_attr8.folders.add(allMA_folder)

    obj_attr9 = MathAttribute(name='Тип Задачи 1', mathtype='TaskType')
    obj_attr9.save()
    obj_folder = MathAttribute_Folder.objects.get(system_name='TASKTYPES')
    allMA_folder = MathAttribute_Folder.objects.get(system_name='ALL_MATHATTRIBUTES')
    obj_attr9.folders.add(obj_folder)
    obj_attr9.folders.add(allMA_folder)

    obj_attr10 = MathAttribute(name='Тип Задачи 2', mathtype='TaskType')
    obj_attr10.save()
    obj_folder = MathAttribute_Folder.objects.get(system_name='TASKTYPES')
    allMA_folder = MathAttribute_Folder.objects.get(system_name='ALL_MATHATTRIBUTES')
    obj_attr10.folders.add(obj_folder)
    obj_attr10.folders.add(allMA_folder)

    obj_source1 = Source(name='BOOK_1')
    obj_source1.save()

    obj_source2 = Source(name='BOOK_2')
    obj_source2.save()

    obj_source3 = Source(name='BOOK_3')
    obj_source3.save()

    obj_tn1=TaskNumber(body = '1', source = obj_source1)
    obj_tn1.save()

    obj_tn2 = TaskNumber(body='2', source = obj_source1)
    obj_tn2.save()


    obj_tn3 = TaskNumber(body='1', source = obj_source2)
    obj_tn3.save()


    obj_tn4 = TaskNumber(body='2', source = obj_source2)
    obj_tn4.save()


    obj_tn5 = TaskNumber(body='1', source = obj_source3)
    obj_tn5.save()

    obj_tn6 = TaskNumber(body='2', source = obj_source3)
    obj_tn6.save()

    obj_task1 = Task(body='1+1', ans='2')
    obj_task1.save()
    obj_task1.taskNumber.add(obj_tn1)

    obj_task2 = Task(body='2+2', ans='4')
    obj_task2.save()
    obj_task2.taskNumber.add(obj_tn2)

    obj_task3 = Task(body='3+3', ans='6')
    obj_task3.save()
    obj_task3.taskNumber.add(obj_tn3, obj_tn6)

    obj_task4 = Task(body='4+4', ans='8')
    obj_task4.save()
    obj_task4.taskNumber.add(obj_tn4)

    obj_task5 = Task(body='5+5', ans='10')
    obj_task5.save()
    obj_task5.taskNumber.add(obj_tn5, obj_tn1)

    obj_task6 = Task(body='6+6', ans='12')
    obj_task6.save()
    obj_task6.taskNumber.add(obj_tn6)

    obj = Solution(body='Решение А', name='Способ 1')
    obj.save()
    obj.task = (obj_task1)
    obj.mathAttribute.add(obj_attr1)
    obj.mathAttribute.add(obj_attr5)
    obj.save()

    obj = Solution(body='Решение Б', name='Способ 2')
    obj.save()
    obj.task = (obj_task1)
    obj.mathAttribute.add(obj_attr2)
    obj.mathAttribute.add(obj_attr6)
    obj.save()

    obj = Solution(body='Решение В', name='Способ 1')
    obj.save()
    obj.task = (obj_task2)
    obj.mathAttribute.add(obj_attr7)
    obj.mathAttribute.add(obj_attr3)
    obj.mathAttribute.add(obj_attr2)
    obj.save()

    obj = Solution(body='Решение В', name='Способ 1')
    obj.save()
    obj.task = (obj_task3)
    obj.mathAttribute.add(obj_attr2, obj_attr9, obj_attr7)
    obj.save()

    obj = Solution(body='Решение В', name='Способ 1')
    obj.save()
    obj.task = (obj_task4)
    obj.mathAttribute.add(obj_attr1,obj_attr10,obj_attr4)
    obj.save()

    obj = Solution(body='Решение В', name='Способ 1')
    obj.save()
    obj.task = (obj_task5)
    obj.mathAttribute.add(obj_attr1,obj_attr2,obj_attr7)
    obj.save()

    obj = Solution(body='Решение В', name='Способ 1')
    obj.save()
    obj.task = (obj_task6)
    obj.mathAttribute.add(obj_attr5,obj_attr6,obj_attr4,obj_attr8,obj_attr10)
    obj.save()

