# Generated by Django 5.0.4 on 2024-04-13 17:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0011_remove_jobtitle_department_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobtitle',
            name='department',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='production.department'),
        ),
    ]