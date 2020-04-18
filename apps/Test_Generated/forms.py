from django.forms import ModelForm
from apps.Main.models import Test_Template


# Класс формы шаблона тестов задач
class TestTemplateForm(ModelForm):
    class Meta:
        model = Test_Template
        fields = ('name', 'comment', 'folders_and_numbers', 'is_permanent')
