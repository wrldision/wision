# Generated by Django 3.2.4 on 2021-10-24 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Besoin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=40)),
                ('resume', models.CharField(max_length=255)),
                ('description', models.TextField(default='Aucune Description')),
                ('type', models.CharField(choices=[('ch1', 'Don en Nature'), ('ch2', 'Don en Espèces')], max_length=40)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('update_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Don',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref', models.CharField(blank=True, max_length=12)),
                ('type', models.CharField(choices=[('ch1', 'Don en Nature'), ('ch2', 'Don en Espèces')], max_length=40)),
                ('montant', models.IntegerField(help_text='Valeur en Dollars (USD)')),
                ('detail', models.TextField(default='Aucun Detail')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('update_at', models.DateField(auto_now=True)),
            ],
        ),
    ]
