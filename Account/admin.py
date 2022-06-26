from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

from Account.models import AdminUser, City, Unit
# Register your models here.
User = get_user_model()
admin.site.register(User)
admin.site.register(AdminUser)

admin.site.register(City)
admin.site.register(Unit)
admin.site.unregister(Group)