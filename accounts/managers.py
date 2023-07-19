from django.contrib.auth.base_user import BaseUserManager
from . import models


class UserManager(BaseUserManager):
    def create_user(self, phone, firstname, email, lastname ,passwd=None, password=None):
        if not phone:
            raise ValueError('Users must have a Phone')
        user = self.model(
            phone=phone,
            firstname=firstname,
            lastname=lastname,
            decrypted_password = passwd
        )
        
        user.set_password(password)
        user.email = email
        user.save(using=self._db)
        return user

    def create_superuser(self, phone ,firstname, lastname, password=None):

        user = self.create_user(
            phone,
            firstname,
            lastname,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
