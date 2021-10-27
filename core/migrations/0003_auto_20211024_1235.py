# Generated by Django 3.2.4 on 2021-10-24 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gerant', '0001_initial'),
        ('core', '0002_besoin_image_mise_en_avant'),
    ]

    operations = [
        migrations.AddField(
            model_name='besoin',
            name='gerant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gerant.gerant'),
        ),
        migrations.AlterField(
            model_name='don',
            name='montant',
            field=models.IntegerField(help_text='Valeur en Dollars Americain(1 USD = 560FCA)'),
        ),
    ]