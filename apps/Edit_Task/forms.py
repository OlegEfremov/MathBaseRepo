from django import forms

from apps.Main.models import UploadedTaskImages, UploadedSolImages


class TaskForm(forms.Form):

    body = forms.CharField(widget = forms.Textarea(attrs={'class': 'form-control', 'rows': 3}), required=True)
    ans = forms.CharField(widget = forms.Textarea(attrs={'class': 'form-control', 'rows': 2}), required=False)


# Форма загрузки рисунков для условий задач
class TaskImagesUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedTaskImages
        fields = ['name', 'image']



