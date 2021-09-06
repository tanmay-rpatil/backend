# Generated by Django 3.2.5 on 2021-09-06 19:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0002_application'),
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analytics',
            name='data',
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='device',
            name='properties',
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='schema',
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='sensor_reading',
            name='data',
            field=models.JSONField(default=dict),
        ),
        migrations.CreateModel(
            name='Sensor_Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='accounts.application')),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.sensor')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contents', models.JSONField(default=dict)),
                ('target_device', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.device')),
            ],
        ),
    ]