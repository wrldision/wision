# Generated by Django 3.2.4 on 2021-10-24 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gerant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gerant',
            name='avatar',
            field=models.ImageField(default='avatar.png', upload_to='avatars'),
        ),
    ]
