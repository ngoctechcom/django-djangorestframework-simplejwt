from pydoc import describe
from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=255)
    describe = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
