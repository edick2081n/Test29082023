from django.db import models

class Flat(models.Model):
    square = models.FloatField()
    bedroom = models.IntegerField()
    bath = models.IntegerField()

    def __str__(self):
        return str(self.square)

