from django import forms

from apps.Main.models import UploadedSolImages


class SolutionForm(forms.Form):

    body = forms.CharField(widget = forms.Textarea(attrs={'class':'form-control'}), required=True)
    name = forms.CharField(widget = forms.TextInput(attrs={'class':'form-control'}), required=True)


# Форма загрузки рисунков для решений
class SolutionImagesUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedSolImages
        fields = ['name', 'image']
