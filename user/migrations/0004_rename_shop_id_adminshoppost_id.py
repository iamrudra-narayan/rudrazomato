# Generated by Django 4.1.2 on 2022-10-08 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_adminshoppost_shop_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='adminshoppost',
            old_name='shop_id',
            new_name='id',
        ),
    ]
