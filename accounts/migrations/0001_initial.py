# Generated by Django 4.2.1 on 2023-05-18 10:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('firstname', models.CharField(max_length=150, verbose_name='نام')),
                ('lastname', models.CharField(max_length=150, verbose_name='نام خانوادگی')),
                ('phone', models.CharField(max_length=11, unique=True, verbose_name='شماره همراه')),
                ('email', models.CharField(max_length=150, unique=True, verbose_name='ایمیل')),
                ('is_phone_verified', models.BooleanField(default=False, verbose_name='تایید شماره تلفن')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ عضویت')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')),
                ('language', models.CharField(blank=True, default='en', max_length=6, null=True, verbose_name='زبان')),
                ('is_admin', models.BooleanField(default=False, verbose_name='مدیر')),
                ('is_representative', models.BooleanField(default=False, verbose_name='نماینده')),
                ('representation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='user_representation', to=settings.AUTH_USER_MODEL, verbose_name='نماینده کاربر')),
            ],
            options={
                'verbose_name': 'کاربر',
                'verbose_name_plural': 'کاربران',
            },
        ),
        migrations.CreateModel(
            name='BlockUserIP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blocked_ip', models.GenericIPAddressField(verbose_name='IP کاربر')),
            ],
            options={
                'verbose_name': 'IP مسدود',
                'verbose_name_plural': 'IP های مسدود',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='کشور')),
                ('symbol', models.CharField(max_length=150, verbose_name='symbol')),
                ('image', models.ImageField(upload_to='media/')),
            ],
            options={
                'verbose_name': 'کشور',
                'verbose_name_plural': 'کشور ها',
            },
        ),
        migrations.CreateModel(
            name='UserIP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_ip', models.GenericIPAddressField(verbose_name='IP کاربر')),
            ],
            options={
                'verbose_name': 'IP کاربر',
                'verbose_name_plural': 'IP های کاربران',
            },
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='عنوان سرور')),
                ('api_key', models.CharField(max_length=200, verbose_name='کد API')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال/غیر فعال')),
                ('country', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='country', to='accounts.category', verbose_name='کشور')),
            ],
            options={
                'verbose_name': 'سرور',
                'verbose_name_plural': 'سرور ها',
            },
        ),
        migrations.CreateModel(
            name='Representative',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_key', models.CharField(blank=True, max_length=150, null=True, verbose_name='کلید API زرین پال')),
                ('price_by_gb', models.IntegerField(blank=True, default=7000, verbose_name='قیمت بر حسب گیگ')),
                ('traffic_limit', models.IntegerField(blank=True, default=1000, verbose_name='میزان اعتبار')),
                ('traffic_used', models.IntegerField(blank=True, default=0, verbose_name='ترافیک مصرف شده کل')),
                ('representative_name', models.CharField(blank=True, max_length=150, null=True, verbose_name='نام نمایندگی')),
                ('domain', models.CharField(blank=True, max_length=150, null=True, unique=True, verbose_name='دامنه نماینده')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ عضویت')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال/غیرفعال')),
                ('servers', models.ManyToManyField(blank=True, related_name='servers', to='accounts.server', verbose_name='سرور ها')),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
                ('users', models.ManyToManyField(blank=True, related_name='users_of_representative', to=settings.AUTH_USER_MODEL, verbose_name='کاربران نماینده')),
            ],
            options={
                'verbose_name': 'نماینده',
                'verbose_name_plural': 'بخش نمایندگان',
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='نام زبان (فارسی)')),
                ('title_by_language', models.CharField(max_length=150, verbose_name='نام زبان (به زبان انتخابی)')),
                ('symbol', models.CharField(max_length=150, verbose_name='علامت انحصاری (مثال: fa, en, fr)')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال/غیر فعال')),
                ('country', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='language_country', to='accounts.category', verbose_name='کشور')),
            ],
            options={
                'verbose_name': 'زبان',
                'verbose_name_plural': 'زبان ها',
            },
        ),
    ]
