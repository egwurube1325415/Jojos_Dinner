# Generated by Django 3.2.4 on 2021-08-04 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='body',
            field=models.TextField(db_index=True, max_length=1000, verbose_name='Body'),
        ),
    ]
