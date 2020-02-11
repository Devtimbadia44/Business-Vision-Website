# Generated by Django 2.2.5 on 2020-02-11 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0004_remove_productdata_p_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='productdata',
            name='p_desc',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='productdata',
            name='p_name',
            field=models.CharField(choices=[('Mouse', 'MOUSE'), ('Keyboard', 'KEYBOARD'), ('Camera', 'CAMERA'), ('Shirt', 'SHIRT'), ('T Shirt', 'T-SHIRT'), ('Jeans', 'JEANS'), ('Trousers', 'TROUSERS'), ('Bat', 'BAT'), ('Ball', 'BALL'), ('Cap', 'CAP'), ('Pen', 'PEN'), ('Pen Holder', 'PEN HOLDER'), ('Paper Weight', 'PAPER WEIGHT'), ('White Board', 'WHITE BOARD'), ('Table Fan', 'TABLE FAN'), ('Showcase', 'SHOWCASE'), ('Air Purifier', 'AIR PURIFIER')], default='Mouse', max_length=25),
        ),
        migrations.AlterField(
            model_name='productdata',
            name='seller_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
