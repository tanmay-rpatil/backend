# Generated by Django 3.2.5 on 2021-08-23 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='properties',
            field=models.JSONField(default={'error': ''}),
        ),
    ]