from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    time = models.IntegerField()
    difficulty = models.FloatField()
    ingridients = models.CharField(max_length=1000)
    description = models.CharField(max_length=5000)

    def __str__(self):
        return self.name