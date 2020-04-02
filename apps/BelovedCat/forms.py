from django import forms


class CatForm(forms.Form):

    answer = forms.CharField(widget = forms.TextInput(attrs={'class':'form-control'}), required=False)

