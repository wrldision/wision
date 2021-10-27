# Generated by Django 3.2.4 on 2021-10-24 12:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Donateur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(default='Aucune biographie...')),
                ('email', models.EmailField(max_length=254)),
                ('nom', models.CharField(max_length=40)),
                ('prenom', models.CharField(max_length=40)),
                ('avatar', models.ImageField(default='avatar.png', upload_to='avatars')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('update_at', models.DateField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]