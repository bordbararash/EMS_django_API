from django.contrib.auth.base_user import BaseUserManager


class MyUserManager(BaseUserManager):
    def create_user(self, User_mobile, password=None, **other_fields):
        if not User_mobile:
            raise ValueError('User_mobile is required!!')
        # in settings you should set :AUTH_USER_MODEL
        user = self.model(User_mobile=User_mobile, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, User_mobile, password=None, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('superuser must is_staff=True!!! ')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('superuser must be is_superuser=True!!! ')
        return self.create_user(User_mobile,password, **other_fields)
