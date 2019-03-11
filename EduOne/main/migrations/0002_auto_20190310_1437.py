# Generated by Django 2.1.7 on 2019-03-10 06:37

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='apptLocation',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appointment',
            name='apptRejectionReason',
            field=models.CharField(default='-', max_length=200),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='apptStatus',
            field=models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending', max_length=8),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 3, 10, 6, 34, 59, 735181, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='commentDate',
            field=models.DateField(default=datetime.datetime(2019, 3, 10, 6, 34, 59, 719553, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='commentTime',
            field=models.TimeField(default=datetime.datetime(2019, 3, 10, 6, 34, 59, 719553, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='subjectclass',
            name='classOf',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Class'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_parent',
            field=models.BooleanField(default=False, verbose_name='Parent status'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False, verbose_name='Staff status'),
        ),
    ]