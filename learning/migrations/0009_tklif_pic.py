# Generated by Django 4.0.1 on 2022-02-16 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0008_tklif_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='tklif',
            name='pic',
            field=models.ImageField(default=1, upload_to='images/'),
            preserve_default=False,
        ),
    ]
