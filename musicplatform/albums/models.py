from django.db import models
from artists.models import *
from model_utils.models import TimeStampedModel
from imagekit.processors import ResizeToFill
from imagekit.models import ProcessedImageField
from django.core.validators import FileExtensionValidator
class Album(TimeStampedModel):
    artist = models.ForeignKey(Artist, related_name="albums", on_delete=models.CASCADE)
    name = models.CharField(max_length=255,default="New Album")
    release_at = models.DateTimeField()
    cost = models.DecimalField(max_digits=8, decimal_places=2)
    approved = models.BooleanField(default=False, help_text="Approve the album if its name is not explicit")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "albums"


class Song(models.Model):
    album = models.ForeignKey(Album, related_name="songs",on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='static/images',blank=True)
    image_thumbnail = ProcessedImageField(upload_to='static/images', blank=True, processors=[ResizeToFill(100, 50)], format='JPEG',options={'quality': 60})
    audio = models.FileField(upload_to='static/audio', null=True,blank=True,validators=[FileExtensionValidator(allowed_extensions=['mp3', 'wav'])])

    def save(self):
        if not self.name:
         self.name = self.album.name
        super(Song, self).save()
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = "songs"
    