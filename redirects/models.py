from django.db import models

# Create your models here.

class Tracking(models.Model):
    tracking_text = models.CharField(max_length=200)
    tracking_link = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.tracking_text
