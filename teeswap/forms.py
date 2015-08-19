from django import forms

from tee.models import Tee

class qidForm(forms.ModelForm):
    class Meta:
        model = Tee
        fields = ['qid']
