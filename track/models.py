from django.db import models

# Create your models here.

class Track(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    file = models.FileField(upload_to='tracks/')

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'{self.id}. {self.name}'
