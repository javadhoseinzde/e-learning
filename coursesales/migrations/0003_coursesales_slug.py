# Generated by Django 4.0.1 on 2022-02-22 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coursesales', '0002_coursesales_uploadcourse'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursesales',
            name='slug',
            field=models.SlugField(max_length=100, null=True),
        ),
    ]