from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    time = models.IntegerField()
    difficulty = models.FloatField()
    ingridients = models.TextField()
    description = models.TextField()
    photo = models.FileField()
    is_favorite = models.BooleanField(default=False)
    user = models.ForeignKey(User, default=1)

    def get_absolute_url(self):
        return reverse('recipes:detail', kwargs={'pk': self.pk})

    def splitingr(self):
        return (self.ingridients).split(",")

    def __str__(self):
        return self.name


class Comment(models.Model):
    user = models.ForeignKey(User, default=1)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    content = models.TextField()
    time = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.content
