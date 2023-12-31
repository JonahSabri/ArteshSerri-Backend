# Generated by Django 4.2.2 on 2023-07-11 20:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_user_is_main_user_user_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='domain',
        ),
        migrations.AddField(
            model_name='user',
            name='customer_of',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_customer_of', to=settings.AUTH_USER_MODEL, verbose_name='مشتریه کاربر'),
        ),
        migrations.AddField(
            model_name='user',
            name='national_code',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='کد ملی'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_phone_verified',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='تایید شماره تلفن'),
        ),
        migrations.AlterField(
            model_name='user',
            name='users',
            field=models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL, verbose_name='کاربران'),
        ),
    ]
