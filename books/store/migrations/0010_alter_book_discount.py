# Generated by Django 3.2.7 on 2021-10-08 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_alter_book_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='discount',
            field=models.DecimalField(decimal_places=2, default='0', max_digits=7, null=True),
        ),
    ]
