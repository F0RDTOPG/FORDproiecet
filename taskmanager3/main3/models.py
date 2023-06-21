from django.db import models
class Room(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
# Create your models here.

class Room2(models.Model):
    inheritane = models.ForeignKey(Room,on_delete=models.CASCADE)
    trim = models.CharField(max_length=20)
    ore = models.DecimalField(decimal_places=1, max_digits=9)

    def __str__(self):
        return self.trim