# Generated by Django 3.1.5 on 2021-01-29 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoList', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='lists',
            field=models.CharField(default=None, max_length=255),
        ),
    ]
