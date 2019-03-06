# Generated by Django 2.1.7 on 2019-03-06 11:15

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0004_auto_20190213_0559'),
    ]

    operations = [
        migrations.RenameField(
            model_name='announcement',
            old_name='eventDate',
            new_name='dateCreated',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='eventDate',
            new_name='dateFrom',
        ),
        migrations.RemoveField(
            model_name='announcement',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='announcement',
            name='eventTimeFrom',
        ),
        migrations.RemoveField(
            model_name='announcement',
            name='eventTimeTo',
        ),
        migrations.RemoveField(
            model_name='announcement',
            name='isEvent',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='approved',
        ),
        migrations.AddField(
            model_name='announcement',
            name='title',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='announcement',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appointment',
            name='appTitle',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='appointment',
            name='apptStatus',
            field=models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default=1, max_length=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='dateTo',
            field=models.DateField(default='2018-08-01'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.CharField(default='none', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='title',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 3, 6, 11, 13, 13, 424447, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='commentDate',
            field=models.DateField(default=datetime.datetime(2019, 3, 6, 11, 13, 13, 424447, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='commentTime',
            field=models.TimeField(default=datetime.datetime(2019, 3, 6, 11, 13, 13, 424447, tzinfo=utc)),
        ),
    ]