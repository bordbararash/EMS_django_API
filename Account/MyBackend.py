from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import check_password
from django.contrib.auth import get_user_model
from .models import MyUser

class MobileBackend(ModelBackend):
    def authenticate(self,request,username=None,password=None,**kwargs):
        # User = get_user_model()
        # user = User.objects.get(User_mobile=username)
       
        
        
        try:
            
            user=MyUser.objects.filter(User_mobile=username)
            is_active=user.values('is_active')[0]["is_active"]
            user=MyUser.objects.get(User_mobile=username)
            if user.check_password(password) and is_active:
                return user
            else:
                print('USER NOT ACTIVE')
        except (MyUser.DoesNotExist,IndexError):
            return None
    def get_user(self, user_id: int):
        try:
            return MyUser.objects.get(pk=user_id)
        except MyUser.DoesNotExist:
            return None