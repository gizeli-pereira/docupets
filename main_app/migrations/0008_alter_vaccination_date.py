# Generated by Django 4.2 on 2023-05-02 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_remove_visit_vaccines_vaccination_visit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vaccination',
            name='date',
            field=models.DateField(blank=True, verbose_name='Vaccination Date'),
        ),
    ]