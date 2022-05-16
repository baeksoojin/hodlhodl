from django.db import models

# Create your models here.
class Prediction(models.Model):
    prediction_date = models.DateField(primary_key=True)
    close_price = models.FloatField(blank=True, null=True)
    pred_price = models.FloatField()

    class Meta:
        managed = False
        db_table = 'prediction'