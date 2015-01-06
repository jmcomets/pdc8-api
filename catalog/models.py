from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class TreeGenre(models.Model):
    name = models.CharField(max_length=20)
    species = models.CharField(max_length=30)
    type = models.CharField(max_length=15)

    def __unicode__(self):
        return '(%s, %s, %s)' % (self.name, self.species, self.type)

class Tree(models.Model):
    id = models.CharField(max_length=15, primary_key=True)
    name = models.CharField(max_length=50)

    area = models.CharField(max_length=50)
    genre = models.ForeignKey(TreeGenre)

    height = models.IntegerField()         # meters
    trunk_diameter = models.IntegerField() # centimeters
    crown_diameter = models.IntegerField() # meters

    # longitude / latitude (in degrees)
    longitude = models.FloatField(null=True, blank=True,
                                  validators=[MinValueValidator(-180),
                                              MaxValueValidator(180)])
    latitude = models.FloatField(null=True, blank=True,
                                 validators=[MinValueValidator(0),
                                             MaxValueValidator(90)])

    def __unicode__(self):
        return self.name
