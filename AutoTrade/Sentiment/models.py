from django.db import models

# Create your models here.
class Sentiment(models.Model):
    crawling_date = models.DateField(primary_key=True)
    n_count = models.SmallIntegerField()
    p_count = models.SmallIntegerField()
    e_count = models.SmallIntegerField()
    k_val = models.FloatField()
    com_count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sentiment'


class Comments(models.Model):
    crawling_date = models.ForeignKey('Sentiment', models.DO_NOTHING, db_column='crawling_date')
    comment = models.TextField()
    semtiment = models.CharField(max_length=8)
    weight = models.FloatField()

    class Meta:
        managed = False
        db_table = 'comments'

class Topten(models.Model):
    crawling_date = models.ForeignKey(Sentiment, models.DO_NOTHING, db_column='crawling_date')
    word = models.CharField(max_length=50)
    count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'topten'