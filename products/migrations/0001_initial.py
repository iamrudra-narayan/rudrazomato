# Generated by Django 4.1.2 on 2022-10-08 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_category', models.CharField(default='Non-Veg', max_length=40)),
                ('prod_item', models.CharField(default='Biriyani', max_length=40)),
                ('category_image', models.ImageField(default='', upload_to='pics/categoryimages')),
            ],
        ),
        migrations.CreateModel(
            name='FoodProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prod_name', models.CharField(default='Product', max_length=30)),
                ('prod_image', models.ImageField(default='', upload_to='pics/productimages')),
                ('prod_desc', models.TextField(default='', max_length=30)),
                ('marked_price', models.IntegerField()),
                ('discount_price', models.IntegerField()),
                ('selling_price', models.IntegerField()),
                ('item_availability', models.BooleanField(default='')),
                ('prod_category', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='products.category')),
                ('shop', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='user.adminshoppost')),
            ],
        ),
    ]
