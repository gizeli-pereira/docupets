# Generated by Django 4.2 on 2023-05-02 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_grooming'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vaccination',
            name='date',
            field=models.DateField(null=True, verbose_name='Vaccination Date'),
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('date', models.DateField(verbose_name='Visit Date')),
                ('notes', models.CharField()),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.pet')),
                ('vaccines', models.ManyToManyField(to='main_app.vaccination')),
                ('vet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.vet')),
            ],
        ),
    ]
