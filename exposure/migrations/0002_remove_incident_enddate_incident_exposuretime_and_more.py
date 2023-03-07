# Generated by Django 4.1.7 on 2023-03-07 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exposure', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='incident',
            name='enddate',
        ),
        migrations.AddField(
            model_name='incident',
            name='exposuretime',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='incident',
            name='smokecolor',
            field=models.CharField(default=True, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='incident',
            name='smokepresent',
            field=models.BooleanField(default=True, null=True),
        ),
    ]
