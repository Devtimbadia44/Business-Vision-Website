# Generated by Django 2.2.5 on 2020-03-05 14:15

from django.db import migrations, models
import gst_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SellerData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=15)),
                ('gst', gst_field.modelfields.GSTField(max_length=15)),
                ('comp_name', models.CharField(max_length=100)),
                ('address', models.TextField(max_length=200)),
                ('state', models.CharField(max_length=100)),
                ('pincode', models.CharField(max_length=8)),
                ('rating', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=15)),
                ('dob', models.CharField(max_length=15)),
            ],
        ),
    ]
