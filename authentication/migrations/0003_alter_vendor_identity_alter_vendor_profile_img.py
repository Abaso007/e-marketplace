# Generated by Django 4.2.3 on 2023-09-22 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_alter_customuser_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='identity',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='profile_img',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
