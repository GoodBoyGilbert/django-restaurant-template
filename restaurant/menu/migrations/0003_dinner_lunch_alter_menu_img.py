# Generated by Django 4.2.7 on 2024-01-22 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_menu_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dinner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='thumbnails')),
                ('name', models.CharField(max_length=30)),
                ('desc', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('category', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Lunch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='thumbnails')),
                ('name', models.CharField(max_length=30)),
                ('desc', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('category', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='menu',
            name='img',
            field=models.ImageField(upload_to='thumbnails'),
        ),
    ]