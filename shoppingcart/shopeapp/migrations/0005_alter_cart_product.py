# Generated by Django 3.2.9 on 2021-11-04 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopeapp', '0004_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='product',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='shopeapp.product'),
        ),
    ]
