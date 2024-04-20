# Generated by Django 5.0.4 on 2024-04-13 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RunRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateField(auto_now_add=True)),
                ('requester_name', models.CharField(max_length=100)),
                ('requester_phone', models.CharField(max_length=15)),
                ('requester_email', models.CharField(max_length=255)),
                ('requester_department', models.CharField(max_length=100)),
                ('run_date', models.DateField()),
                ('pickup_name', models.CharField(max_length=100)),
                ('pickup_phone', models.CharField(max_length=15)),
                ('pickup_address_1', models.CharField(max_length=100)),
                ('pickup_address_2', models.CharField(max_length=100, null=True)),
                ('pickup_city', models.CharField(max_length=100)),
                ('pickup_state', models.CharField(max_length=2)),
                ('pickup_zip', models.CharField(max_length=10)),
                ('dropoff_name', models.CharField(max_length=100)),
                ('dropoff_phone', models.CharField(max_length=15)),
                ('dropoff_address_1', models.CharField(max_length=100)),
                ('dropoff_address_2', models.CharField(max_length=100, null=True)),
                ('dropoff_city', models.CharField(max_length=100)),
                ('dropoff_state', models.CharField(max_length=2)),
                ('dropoff_zip', models.CharField(max_length=10)),
                ('truck_size', models.CharField(max_length=50, null=True)),
                ('run_details', models.CharField(max_length=500)),
                ('assigned_driver', models.CharField(max_length=100)),
            ],
        ),
    ]
