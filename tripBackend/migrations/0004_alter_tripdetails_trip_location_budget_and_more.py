# Generated by Django 4.1.5 on 2023-01-15 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tripBackend', '0003_alter_tripdetails_trip_location_budget_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tripdetails',
            name='trip_location_budget',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='tripdetails',
            name='trip_members',
            field=models.IntegerField(),
        ),
    ]
