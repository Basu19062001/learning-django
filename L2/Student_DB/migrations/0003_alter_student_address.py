# Generated by Django 5.1.4 on 2024-12-25 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student_DB', '0002_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
    ]
