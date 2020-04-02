from django import forms

class SolutionForm(forms.Form):

    body = forms.CharField(widget = forms.Textarea(attrs={'class':'form-control'}), required=True)
    name = forms.CharField(widget = forms.TextInput(attrs={'class':'form-control'}), required=True)

