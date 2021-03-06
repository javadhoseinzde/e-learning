# Generated by Django 4.0.1 on 2022-02-17 20:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('learning', '0009_tklif_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='TklifAnsser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ansser', models.FileField(upload_to='tklifanser/')),
                ('taklif', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learning.tklif')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
