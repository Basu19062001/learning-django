# Generated by Django 5.1.4 on 2024-12-26 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRUD_Operations', '0002_cars_name_family_email_alter_family_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='cars',
            name='speed',
            field=models.IntegerField(default=50),
        ),
    ]
