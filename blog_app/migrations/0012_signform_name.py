# Generated by Django 4.1.5 on 2023-03-13 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0011_delete_updateprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='signform',
            name='name',
            field=models.CharField(default=2, max_length=255),
            preserve_default=False,
        ),
    ]
