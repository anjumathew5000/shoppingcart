# Generated by Django 3.2.9 on 2021-11-04 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('product_quantity', models.IntegerField()),
                ('product_price', models.IntegerField()),
                ('product_image', models.ImageField(upload_to='images/')),
                ('product_status', models.BooleanField()),
            ],
        ),
    ]