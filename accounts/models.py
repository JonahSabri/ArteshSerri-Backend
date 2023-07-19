from django.shortcuts import get_object_or_404
import jdatetime
from django.contrib.auth.models import AbstractBaseUser
from django.db import models


from .managers import UserManager


class User(AbstractBaseUser):
    firstname = models.CharField(max_length=150, verbose_name="نام")
    lastname = models.CharField(max_length=150, verbose_name="نام خانوادگی")
    phone = models.CharField(max_length=11, unique=True, verbose_name="شماره همراه")
    email = models.CharField(max_length=150, verbose_name="ایمیل", blank=True, null=True)
    is_phone_verified = models.BooleanField(default=False, verbose_name="تایید شماره تلفن",null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ عضویت")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاریخ بروزرسانی")
    is_admin = models.BooleanField(default=False, verbose_name="مدیر")

    objects = UserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['firstname', 'lastname']

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        return self.firstname + " " + self.lastname + " " + self.phone
 
    def jalali_created_at(self):
        jalili_date = jdatetime.date.fromgregorian(date=self.created_at)
        return f"{jalili_date.year}/{jalili_date.month}/{jalili_date.day}"
    jalali_created_at.short_description = "عضویت"

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
    
    def correct_phone(self):
        arabic = '۰١٢٣٤٥٦٧٨٩'
        english = '0123456789'
        translation_table = str.maketrans(arabic, english)

        return translation_table
        

    @property
    def is_staff(self):
        return self.is_admin
