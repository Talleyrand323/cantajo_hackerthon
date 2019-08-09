# Generated by Django 2.2.4 on 2019-08-06 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('gender', models.CharField(max_length=3)),
                ('age', models.CharField(max_length=5)),
                ('catimage', models.ImageField(upload_to='')),
                ('mapimage', models.ImageField(upload_to='')),
                ('info', models.TextField()),
            ],
        ),
    ]
