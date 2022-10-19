from django.db import models
from artists.models import *
from model_utils.models import TimeStampedModel

class Album(TimeStampedModel):
    artist = models.ForeignKey(Artist, related_name="albums", on_delete=models.CASCADE)
    name = models.CharField(max_length=255,default="New Album")
    release_at = models.DateTimeField()
    cost = models.DecimalField(max_digits=8, decimal_places=2,  blank=True)
    approved = models.BooleanField(default=False, help_text="Approve the album if its name is not explicit")

    def __str__(self):
        return self.name