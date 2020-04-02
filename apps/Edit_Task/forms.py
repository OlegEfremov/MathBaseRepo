from django import forms

class TaskForm(forms.Form):

    body = forms.CharField(widget = forms.Textarea(attrs={'class': 'form-control', 'rows': 3}), required=True)
    ans = forms.CharField(widget = forms.Textarea(attrs={'class': 'form-control', 'rows': 2}), required=False)

