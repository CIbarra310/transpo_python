# Generated by Django 5.0.4 on 2024-04-13 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_delete_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='production',
            name='captain_email',
            field=models.EmailField(max_length=254, null=True, verbose_name='email address'),
        ),
        migrations.AddField(
            model_name='production',
            name='captain_name',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='production',
            name='coordinator_email',
            field=models.EmailField(max_length=254, null=True, verbose_name='email address'),
        ),
        migrations.AddField(
            model_name='production',
            name='coordinator_name',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='production',
            name='production_studio',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='production',
            name='prodution_email',
            field=models.EmailField(max_length=254, null=True, verbose_name='email address'),
        ),
        migrations.AddField(
            model_name='production',
            name='purchase_order',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='production',
            name='production_title',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
