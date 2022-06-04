# Generated by Django 4.0.3 on 2022-05-25 05:28
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('semtiment', models.CharField(max_length=8)),
                ('weight', models.FloatField()),
            ],
            options={
                'db_table': 'comments',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sentiment',
            fields=[
                ('crawling_date', models.DateField(primary_key=True, serialize=False)),
                ('n_count', models.SmallIntegerField()),
                ('p_count', models.SmallIntegerField()),
                ('e_count', models.SmallIntegerField()),
                ('k_val', models.FloatField()),
                ('com_count', models.IntegerField()),
            ],
            options={
                'db_table': 'sentiment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Topten',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=50)),
                ('count', models.IntegerField()),
            ],
            options={
                'db_table': 'topten',
                'managed': False,
            },
        ),
    ]
