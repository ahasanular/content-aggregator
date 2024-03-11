from django.db import models
from content_aggregator.utils.mixin import MetaFields
from django.contrib.auth import get_user_model


User = get_user_model()


class Episode(MetaFields):
    title = models.CharField(max_length=200)
    description = models.TextField()
    pub_date = models.DateTimeField()
    link = models.URLField()
    image = models.URLField()
    podcast_name = models.CharField(max_length=100)
    guid = models.CharField(max_length=50)
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None
    )

    def __str__(self) -> str:
        return f"{self.podcast_name}: {self.title}"
