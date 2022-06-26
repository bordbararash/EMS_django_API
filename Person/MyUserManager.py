from django.contrib.auth.base_user import BaseUserManager


class MyUserManager(BaseUserManager):
    def create_user(self, username, password=None, **other_fields):
        if not username:
            raise ValueError('username is required!!')
        # in settings you should set :AUTH_USER_MODEL='authentication.MyBaseUser'
        user = self.model(username=username, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password=None, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('superuser must is_staff=True!!! ')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('superuser must be is_superuser=True!!! ')
        return self.create_user(username, password, **other_fields)
