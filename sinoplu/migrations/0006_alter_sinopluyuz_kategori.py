# Generated by Django 4.2.4 on 2023-10-05 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sinoplu', '0005_sinopluyuz_kategori_alter_sinopluyuz_image1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sinopluyuz',
            name='kategori',
            field=models.CharField(choices=[('egitim', 'Eğitim'), ('saglik', 'Sağlık'), ('insaat', 'İnşaat'), ('gida', 'Gıda'), ('ulasim', 'Ulaşım')], default='Eğitim', max_length=20, verbose_name='Kategori'),
        ),
    ]