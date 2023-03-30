from django.db import models
class Mmodel(models.Model):
    name=models.CharField(max_length=25)
    age=models.IntegerField()
    def __str__(self):
        return self.name
    

# Create your models here.
