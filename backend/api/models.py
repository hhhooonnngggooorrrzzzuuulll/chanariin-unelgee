from django.db import models

class Category(models.Model):
    catid = models.AutoField(primary_key=True)  # Explicit Category ID
    name = models.CharField(max_length=100, unique=True)  # Unique category name

    def __str__(self):
        return self.name

class Service(models.Model):
    serid = models.AutoField(primary_key=True)  # Explicit Service ID
    name = models.CharField(max_length=100)  # Name of the service (e.g., "Haircut", "Manicure")
    description = models.TextField(blank=True, null=True)  # Optional description of the service
    duration = models.PositiveIntegerField()  # Duration in minutes
    price = models.DecimalField(max_digits=6, decimal_places=2)  # Price of the service
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="services")  

    def __str__(self):
        return self.name
