# Generated by Django 4.1.3 on 2023-01-12 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo_app', '0002_login_address_login_age_login_name_login_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='login',
            name='photo',
            field=models.ImageField(null=True, upload_to='profile'),
        ),
        migrations.AddField(
            model_name='login',
            name='qualification',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
