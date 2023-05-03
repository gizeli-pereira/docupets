# Generated by Django 4.2 on 2023-05-03 00:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_alter_visit_vaccines'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visit',
            name='vaccines',
        ),
        migrations.AddField(
            model_name='vaccination',
            name='visit',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main_app.visit'),
            preserve_default=False,
        ),
    ]
