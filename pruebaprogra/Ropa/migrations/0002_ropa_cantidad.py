# Generated by Django 4.1.3 on 2022-11-27 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ropa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ropa',
            name='cantidad',
            field=models.CharField(default=2, max_length=20),
            preserve_default=False,
        ),
    ]
