from django.db import models

class  Artist(models.Model):
    Stage_name = models.CharField(max_length=255, unique=True, blank=True)
    Social_link = models.URLField(max_length=200,null=False)
    
    def __str__(self):
        return self.Stage_name
    
    class Meta:
        ordering = ['Stage_name']
