# Generated by Django 5.1.4 on 2024-12-25 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student_DB', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
