# Generated by Django 4.1.6 on 2023-03-04 07:21

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='add',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('description', models.TextField()),
                ('created_by', models.CharField(max_length=222)),
            ],
        ),
    ]
