# Generated by Django 4.0.1 on 2022-02-05 08:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(null=True, unique=True, verbose_name='ادرس دوره')),
                ('name', models.CharField(max_length=100, verbose_name='اسم دوره')),
                ('text', models.TextField(verbose_name='توضیحات')),
                ('level', models.CharField(max_length=50, verbose_name='سطح کلاس')),
                ('time', models.DateField(verbose_name='تاریخ شروع')),
                ('term_number', models.IntegerField(verbose_name='شماره ترم')),
                ('start_time', models.CharField(max_length=100, verbose_name='ساعت کلاس')),
                ('Status', models.CharField(choices=[('p', 'منتشر شده'), ('d', 'پیش نویس')], default='d', max_length=10, verbose_name='وضعیت')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Courses', to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
        ),
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='corses', to='learning.course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]