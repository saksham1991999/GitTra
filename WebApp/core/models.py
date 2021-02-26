from googletrans import LANGUAGES
from django.db import models


language_choices = []
for key, value in LANGUAGES.items():
    language_choices.append((key, value.title()))
language_choices = tuple(language_choices)


class Repository(models.Model):
    url = models.URLField(blank=True, null=True)
    file = models.FileField(blank=True, null=True)
    translated = models.FileField(blank=True, null=True)
    language = models.CharField(max_length=5, choices=language_choices)
    directory = models.CharField(blank=True, null=True, max_length=512)

    class Meta:
        verbose_name_plural = "Repositories"
