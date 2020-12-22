# Generated by Django 3.0.2 on 2020-02-28 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0006_auto_20200227_2109'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemlist',
            name='Category',
            field=models.CharField(choices=[('ELEC', 'Electronics'), ('STAT', 'Stationary'), ('CLOTH', 'Clothes'), ('FTW', 'Footwear'), ('BAGS', 'Bags'), ('OTHER', 'Other')], default='OTHER', max_length=5),
        ),
    ]
