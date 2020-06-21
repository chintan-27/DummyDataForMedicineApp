from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Medicine(models.Model):
    name = models.CharField(max_length=100)
    remaininginstock = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    image = models.ImageField(upload_to='img/')
    amountperpack = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    type = models.CharField(max_length=100)
    amountperdosage = models.FloatField()
    price = models.FloatField(default=0.0)
    manufacturer = models.CharField(max_length=150)

    def __str__(self):
        return self.name
