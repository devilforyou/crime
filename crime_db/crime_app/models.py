from django.db import models

class Criminal(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    crime = models.CharField(max_length=200)
    jail_location = models.CharField(max_length=100)
    cell_no = models.IntegerField()
    health_condition = models.TextField(blank=True)

    def __str__(self):
        return self.name