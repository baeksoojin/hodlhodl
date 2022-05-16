from django.db import models

# Create your models here.
class Prediction(models.Model):
    prediction_date = models.DateField(null=False)
    close_price = models.FloatField(blank=True, null=True)
    pred_price = models.FloatField(null=False)

    class Meta:
        managed = True
        db_table = 'prediction'