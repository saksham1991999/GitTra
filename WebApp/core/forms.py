from django import forms

from .models import Repository


class RepositoryForm(forms.ModelForm):
    class Meta:
        model = Repository
        fields = (
            "file",
            "url",
            "language",
        )

