# Generated by Django 2.2 on 2019-04-17 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_my_card'),
    ]

    operations = [
        migrations.AlterField(
            model_name='my_card',
            name='name',
            field=models.TextField(max_length=50),
        ),
    ]