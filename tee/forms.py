from django import forms

from tee.models import Tee

class teeForm(forms.ModelForm):
    class Meta:
        model = Tee
        exclude = []
        widgets = {'qid': forms.HiddenInput(), 'traded': forms.HiddenInput()}


class teeForm2(forms.ModelForm):
    class Meta:
        model = Tee
        fields = ['qid', 'traded']
        widgets = {'qid': forms.HiddenInput()}
