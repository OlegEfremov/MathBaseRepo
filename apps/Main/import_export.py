from apps.Main.models import TaskNumber, Task


def many_to_many_link():
    i = 523
    j=2107
    while i<=1031:
        task_number = TaskNumber.objects.get(id=i)
        task = Task.objects.get(id=j)

        task.taskNumber.add(task_number)
        task.save()

        i += 1
        j += 1

