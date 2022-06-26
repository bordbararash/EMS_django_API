# from django.contrib import admin
# from .models import Person,Profile,Relation
# from django.contrib.auth import get_user_model

# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# # Register your models here.
# Person=get_user_model()

# class PersonAdmin(BaseUserAdmin):
   
#     model = Person
#     search_fields = ('email', 'first_name', 'last_name',)
#     list_display = ('username','first_name', 'last_name', 'gender','User_national_code', 'User_mobile','thumbnail_tag','jUser_reg_dateTime')
#     list_filter = ()
#     ordering = ('date_joined',)
#     fieldsets = (
#         (None, {'fields': ('first_name','last_name','gender')})
#         ,
#         ('Personal Information', {'fields': ('User_mobile', 'User_national_code','User_personal_Img')}),
#     )
#     # add_fieldsets = (
#     #     (None, {'fields': ( 'username','first_name', 'last_name', 'gender','User_national_code', 'User_mobile','email','User_personal_Img')}),
        
#     # )
#     add_fieldsets = (
#         ('Personal Info', {'fields': ( 'first_name',  'last_name', 'username' ,'password1', 'password2' )}),
#         ('Other Info', {'fields': ('gender','User_mobile', 'User_national_code', 'User_personal_Img', 'email' )}),
        
#     )

# admin.site.register(Person,PersonAdmin)
# admin.site.register(Profile)
# admin.site.register(Relation)