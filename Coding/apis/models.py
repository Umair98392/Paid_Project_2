from django.db import models

class localityDescription(models.Model):
    Id = models.IntegerField(primary_key=True)
    MSSubClass = models.IntegerField()
    MSZoning = models.CharField(max_length=21, blank=False, default='')
    LotFrontage = models.IntegerField()
    LotArea = models.IntegerField()
    Street = models.CharField(max_length=21, blank=False, default='')
    Alley =  models.CharField(max_length=21, blank=False, default='')
    LotShape = models.CharField(max_length=21, blank=False, default='')
    LandContour = models.CharField(max_length=21, blank=False, default='')
    Utilities = models.CharField(max_length=21, blank=False, default='')
    LotConfig = models.CharField(max_length=21, blank=False, default='')
    LandSlope = models.CharField(max_length=21, blank=False, default='')
    Neighborhood = models.CharField(max_length=21, blank=False, default='')
