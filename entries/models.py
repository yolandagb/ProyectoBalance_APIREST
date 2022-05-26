from django.db import models

# Create your models here.
class EntryModel(models.Model):
    datetime = models.DateTimeField()
    concept= models.CharField(max_length=255)
    amount = models.FloatField()
    
    
    