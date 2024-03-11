from django.db import models
from content_aggregator.utils.mixin import MetaFields


class ContactMessage(MetaFields):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f'{self.name} - {self.email}'

