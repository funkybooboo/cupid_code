# Generated by Django 5.0.2 on 2024-03-20 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20240221_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dater',
            name='profile_picture',
            field=models.ImageField(height_field=24, null=True, upload_to='api/images', width_field=24),
        ),
    ]
