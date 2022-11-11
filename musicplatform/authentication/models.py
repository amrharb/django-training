from django.db import models
from users.models import User

# Create your models here.


class Artist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name="artists")
    stage_name = models.CharField(blank=False, unique=True, max_length=255)
    social_link_field = models.URLField(max_length=255, blank=True)

    def approved_albums(self):
        return self.album_set.filter(is_approved=True).count()

    def __str__(self):
        return (f"stage_name = {self.stage_name} || social_link_field = {self.social_link_field}")