# Generated by Django 4.0.4 on 2022-06-28 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0016_producto_codigo_producto_color_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.IntegerField(default=0),
        ),
    ]
