# Generated by Django 5.0.2 on 2024-03-21 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_dater_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dater',
            name='profile_picture',
            field=models.ImageField(null=True, upload_to='api/images'),
        ),
    ]
