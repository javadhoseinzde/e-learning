# Generated by Django 4.0.1 on 2022-02-17 20:06

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('learning', '0010_tklifansser'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TklifAnsser',
            new_name='TklifAnswer',
        ),
    ]
