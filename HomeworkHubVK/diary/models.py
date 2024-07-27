from django.db import models


class Homework(models.Model):
    discipline = models.CharField(max_length=50)
    date = models.DateField()

    def __str__(self):
        return self.discipline
