# Generated by Django 5.0.2 on 2024-03-02 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='information',
            name='content',
            field=models.TextField(default=''),
        ),
    ]