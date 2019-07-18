from django.db import models

# Create your models here.
class Picture(models.Model):
    picture = models.FileField(blank=False, null=False)
    name = models.CharField(max_length=50)
    detail = models.CharField(max_length=50)
