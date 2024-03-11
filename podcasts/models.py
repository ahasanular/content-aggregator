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
    user = models.ManyToManyField(
        User,
        null=True,
        blank=True,
        default=None,
        related_name='user_episodes'
    )
    # objects = EpisodeManager()

    def __str__(self) -> str:
        return f"{self.id} - {self.podcast_name}: {self.title}"
