# Generated by Django 3.1.7 on 2021-05-31 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0038_reg'),
    ]

    operations = [
        migrations.AddField(
            model_name='reg',
            name='is_reg',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
