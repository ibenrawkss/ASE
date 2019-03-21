# Generated by Django 2.1.7 on 2019-03-12 06:05

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 3, 12, 6, 5, 44, 578072, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='commentDate',
            field=models.DateField(default=datetime.datetime(2019, 3, 12, 6, 5, 44, 577566, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='commentTime',
            field=models.TimeField(default=datetime.datetime(2019, 3, 12, 6, 5, 44, 577585, tzinfo=utc)),
        ),
    ]