from django.db import models

# Create your models here.
class Detect(models.Model):
    prediction_date = models.DateTimeField()
    close_chg = models.FloatField()
    sell = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'detect'

class Result(models.Model):
    result_date = models.DateField(primary_key=True)
    hpr_percent = models.FloatField()
    mdd = models.FloatField(db_column='MDD')  # Field name made lowercase.
    buy_hold_hpr_percent = models.FloatField()
    buy_hold_mdd = models.FloatField(db_column='buy_hold_MDD')  # Field name made lowercase.
    buy_price = models.FloatField()
    sell_price = models.FloatField()

    class Meta:
        managed = False
        db_table = 'result'