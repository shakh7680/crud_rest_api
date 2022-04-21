from django.db import models
from django.contrib.auth.models import User
from django.utils.text import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields



class Post(TranslatableModel):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    translations = TranslatedFields(
        title=models.CharField(max_length=50, verbose_name=_("Title"))
    )

    def __str__(self):
        return self.safe_translation_getter("title")