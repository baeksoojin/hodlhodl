from django.db import models

# Create your models here.
class Prediction(models.Model): # lstm model result 
    prediction_date = models.DateField(null=False)
    close_price = models.FloatField(blank=True, null=True)
    pred_price = models.FloatField(null=False)

    class Meta:
        managed = True
        db_table = 'prediction'

class Adaboost(models.Model): # Adaboost model result 
    prediction_date = models.DateField()
    close_price = models.FloatField()
    pred_price = models.FloatField()

    class Meta:
        managed = False
        db_table = 'Adaboost'
