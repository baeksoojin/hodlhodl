from django.db import models

# Create your models here.
class Sentiment(models.Model):
    crawling_date = models.DateField(primary_key=True)
    n_count = models.SmallIntegerField()
    p_count = models.SmallIntegerField()
    e_count = models.SmallIntegerField()
    k_val = models.FloatField()
    com_count = models.IntegerField()
    n_vcount = models.SmallIntegerField()
    p_vcount = models.SmallIntegerField()
    e_vcount = models.SmallIntegerField()
    com_vcount = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'sentiment'


class Comments(models.Model):
    crawling_date = models.ForeignKey('Sentiment', models.DO_NOTHING, db_column='crawling_date')
    comment = models.TextField()
    sentiment = models.CharField(max_length=8)
    weight = models.FloatField()
    vote = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'comments'

class WordcloudTable(models.Model):
    crawling_date = models.ForeignKey(Sentiment, models.DO_NOTHING, db_column='crawling_date')
    word = models.CharField(max_length=50)
    count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wordcloud_table'