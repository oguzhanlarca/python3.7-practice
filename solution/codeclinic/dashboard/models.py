from django.db import models

class DashboardData(models.Model):
    timestamp = models.DateTimeField()
    pulsometer_readout = models.IntegerField()
    engine_efficiency = models.FloatField()
    red_value = models.IntegerField()
    blue_value = models.IntegerField()
    green_value = models.IntegerField()
