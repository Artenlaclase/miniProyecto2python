from django.db import models

# Create your models here.

class Manufacturer(models.Model):
    marca = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    start_date = models.DateField()
    webpage = models.URLField()

    def __str__(self):
        return self.marca

class Smartphone(models.Model):
    name_smartphone = models.CharField(max_length=200)
    marca = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    ram = models.CharField(max_length=5)
    storage = models.CharField(max_length=5)
    Screen_size = models.CharField(max_length=5)

