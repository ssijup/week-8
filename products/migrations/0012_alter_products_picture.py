# Generated by Django 4.1.5 on 2023-02-09 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_alter_products_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='picture',
            field=models.ImageField(upload_to='media/'),
        ),
    ]