# Generated by Django 3.2 on 2021-04-24 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceapp', '0002_auto_20210421_0745'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name'], 'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='product'),
        ),
    ]