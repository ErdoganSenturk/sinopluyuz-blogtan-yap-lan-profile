# Generated by Django 4.2.4 on 2023-10-09 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sinoplu', '0008_remove_sinopluyuz_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='sinopluyuz',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]