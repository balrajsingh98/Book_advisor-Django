from django.db import models

# Create your models here.

class Advisor(models.Model):

    AdvisorName = models.CharField(max_length=80)
    AdvisorPhotoURL = models.URLField(max_length=80)


