# Generated by Django 2.2.4 on 2019-08-06 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_map', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catlist',
            name='catimage',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='catlist',
            name='mapimage',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
