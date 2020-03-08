from django import forms
from codemirror import CodeMirrorTextarea


widget = CodeMirrorTextarea(
    mode="python",
)


class SampleForm(forms.Form):
    # body = forms.CharField(label="Bodssy", widget=widget)
    body = forms.CharField(label ="",  widget=widget)
