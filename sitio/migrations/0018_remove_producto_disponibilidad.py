# Generated by Django 4.0.4 on 2022-06-28 19:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0017_alter_producto_precio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='disponibilidad',
        ),
    ]