# Generated by Django 3.0.8 on 2020-07-23 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_auto_20200720_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitor',
            name='photo',
            field=models.ImageField(upload_to='visitors'),
        ),
    ]
