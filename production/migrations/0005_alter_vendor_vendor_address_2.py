# Generated by Django 5.0.4 on 2024-04-13 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0004_production_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='vendor_address_2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
