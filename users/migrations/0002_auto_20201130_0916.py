# Generated by Django 3.1.3 on 2020-11-30 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='contact',
            field=models.PositiveIntegerField(blank=True, null=True, unique=True),
        ),
    ]
