# Generated by Django 5.0.4 on 2024-04-13 03:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_production_captain_email_production_captain_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='production',
            old_name='prodution_email',
            new_name='production_email',
        ),
    ]