from django.db import models
# Create your models here.

#Reception Hall Package class

class ReceptionHallPackage(models.Model):
    RH_packageID    = models.IntegerField
    theme           = models.CharField(max_length=20)
    price           = models.FloatField(max_length=10)
    description     = models.CharField(max_length=30)



#Reception Hall reservation class

class ReceptionHallBook(models.Model):
    RH_reserveID    = models.IntegerField
    cusId           = models.CharField(max_length=10)
    theme           = models.CharField(max_length=20)
    date            = models.DateField
    timeFrom        = models.CharField
    timeTo          = models.TimeField

    


