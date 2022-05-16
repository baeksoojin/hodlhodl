from django.db import models

# Create your models here.
class Sentiment(models.Model):
    crawling_date = models.DateField(primary_key=True)
    n_count = models.SmallIntegerField()
    p_count = models.SmallIntegerField()
    neu_count = models.SmallIntegerField()
    k_val = models.FloatField()

    class Meta:
        managed = False
        db_table = 'sentiment'


class Comments(models.Model):
    crawling_date = models.ForeignKey('Sentiment', models.DO_NOTHING, db_column='crawling_date')
    comment = models.TextField()
    sentiment = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'comments'