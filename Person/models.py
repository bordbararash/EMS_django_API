# from django.utils.html import format_html
# from django.db import models
# from Account.models import MyUser
# from Utils.general_model import GeneralModel
# from django.contrib.auth.models import User, AbstractUser
# from Account.models import MyUser
# from .MyUserManager import MyUserManager
# from django.core import validators
# from django.utils.deconstruct import deconstructible
# from django.utils.translation import gettext_lazy as _
# from django.contrib.auth import get_user_model
# # # Create your models here.




# @deconstructible
# class UnicodeUsernameValidator(validators.RegexValidator):
#     regex = r"^[\w.@+-]+\Z"
     
#     message = _(
#         "Enter a valid username. This value may contain only letters, "
#         "numbers, and @/./+/-/_ characters."
#     )
#     flags = 0

# class Person(AbstractUser):

#     USERNAME_FIELD = 'username'
    

    

#     username_validator = UnicodeUsernameValidator()
#     username = models.CharField(
#         _("username"),
#         max_length=150,
#         unique=True,
        
#         help_text=_(
#             "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
#         ),
#         validators=[username_validator],
#         error_messages={
#             "unique": _("A user with that username already exists."),
#         },
#     )
#     
#     User_national_code = models.CharField(
#         max_length=10, verbose_name='کد ملی ',unique=True)
#     User_mobile = models.CharField(
#         max_length=11, verbose_name='شماره موبایل',unique=True)
#     User_personal_Img = models.ImageField(
#         upload_to=upload_image_path, null=True, blank=True, verbose_name='عکس پرسنلی  ')

#     # hits = models.ManyToManyField(SportField, through="SportFieldStudent", blank=True, related_name='hits', verbose_name='بازدیدها')

#     def thumbnail_tag(self):
#         if self.User_personal_Img:
#             return format_html("<img width=60 height=60 style='border-radius: 5px;' src='{}'>".format(self.User_personal_Img.url))
#         else:
#             return format_html("<img width=60 height=60 style='border-radius: 5px' src='{}'>".format('..\..\..\media\custom_login\imgStu\default.png'))
#     thumbnail_tag.short_description = "تصویر کاربر"

#     def jUser_reg_dateTime(self):
#         return jalali_converter(self.date_joined)
#     jUser_reg_dateTime.short_description = "زمان  ثبت نام"

#     class Meta:
#         verbose_name_plural = 'کاربران '
#         verbose_name = 'کاربر '
#         ordering = ['-date_joined']

#     def __str__(self):
#         return self.first_name + " " + self.last_name

#     objects: MyUserManager()


# class Relation(models.Model):
#     from_user = models.ForeignKey(
#         Person, on_delete=models.CASCADE, related_name='followers')
#     to_user = models.ForeignKey(
#         Person, on_delete=models.CASCADE, related_name='following')
#     created = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f'{self.from_user} following {self.to_user}'




# ============
# class IsActiveUserManager(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset().filter(is_active=True)

# class MyBaseUser(AbstractUser):

#     username = None
#     email =None
#     date_joined = models.DateTimeField(auto_now_add=True)
#     last_login = models.DateTimeField(auto_now_add=True)
#     Date_uniqueCode_created = models.DateTimeField(auto_now_add=True)
#     ConfirmEmailCode = models.IntegerField(
#         null=True, blank=True, verbose_name="کد تایید ایمیل")
#     IsConfirmEmail = models.BooleanField(
#         null=True, blank=True, default=False, verbose_name="ایمیل تایید شده/نشده")
#     UniqueCode = models.CharField(
#         null=True, blank=True, max_length=500, verbose_name='کد منحصر به فرد')
#     User_national_code = models.CharField(
#         max_length=10, verbose_name='کد ملی ')
#     User_mobile = models.CharField(
#         max_length=11, verbose_name='شماره موبایل')
#     User_email = models.CharField(
#         max_length=20, verbose_name='ایمیل',unique=True)

#     REQUIRED_FIELDS = ['last_name', 'first_name', 'User_email']

#     def __str__(self):
#         return self.User_email

#     def jdate_joined(self):
#         return jalali_converter(self.date_joined)
#     jdate_joined.short_description = "تاریخ عضویت"

#     def jlast_login(self):
#         return jalali_converter(self.last_login)
#     jlast_login.short_description = "زمان آخرین ورود"

#     objects = MyUserManager()
#     USERNAME_FIELD = 'User_email'
#     REQUIRED_FIELDS = []

#     backend = 'authentication.myBackend.EmailBackend'

#     is_active_objects = IsActiveUserManager()  # The specific manager.


# =========================
# from django.db import models
# from django.contrib.auth.models import AbstractUser, User
# import os
# import random
# import string
# from extensions.utils import jalali_converter
# from django.core.validators import MaxValueValidator, MinValueValidator
# from django.contrib  import auth


# def get_filename_ext(filepath):
#     base_name = os.path.basename(filepath)
#     name, ext = os.path.splitext(base_name)
#     return name, ext


# def upload_image_path(instance, filename):
#     name, ext = get_filename_ext(filename)
#     file_name = ''.join(random.choice(string.ascii_lowercase) for i in range(16))
#     final_name = f"{file_name}{ext}"
#     return f"custom_login/imgStu/{final_name}"


# class University(models.Model):
#     University_name = models.CharField(max_length=50,verbose_name=' نام دانشگاه',unique=True)
#     University_dateTime = models.DateTimeField(verbose_name='تاریخ ورود اطلاعات',auto_now_add=True)
#     def jUniversity_dateTime(self):
# 	    return jalali_converter(self.University_dateTime)
#     jUniversity_dateTime.short_description = "زمان ورود اطلاعات"

#     def __str__(self):
#         return self.University_name
#     class Meta:
#         verbose_name_plural = 'دانشگاهها'
#         verbose_name = 'دانشگاه '
#         ordering = ['-University_name']

# class SportField(models.Model):
#     SportField_name = models.CharField(max_length=30,verbose_name='رشته ورزشی',unique=True)
#     SportField_dateTime = models.DateTimeField(verbose_name='تاریخ ورود اطلاعات',auto_now_add=True)
#     def jSportField_dateTime(self):
# 	    return jalali_converter(self.SportField_dateTime)
#     jSportField_dateTime.short_description = "زمان ورود اطلاعات"


#     def __str__(self):
#         return self.SportField_name
#     class Meta:
#         verbose_name_plural = 'رشته های ورزشی '
#         verbose_name = 'رشته ورزشی '
#         ordering = ['-SportField_name']


# class AcademicField(models.Model):
#     AcademicField_name = models.CharField(max_length=30,verbose_name='رشته تحصیلی',unique=True)
#     AcademicField_dateTime = models.DateTimeField(verbose_name='تاریخ ورود اطلاعات',auto_now_add=True)
#     def jAcademicField_dateTime(self):
# 	    return jalali_converter(self.AcademicField_dateTime)
#     jAcademicField_dateTime.short_description = "زمان ورود اطلاعات"


#     def __str__(self):
#         return self.AcademicField_name
#     class Meta:
#         verbose_name_plural = ' رشته های تحصیلی'
#         verbose_name = ' رشته تحصیلی'
#         ordering = ['-AcademicField_name']

# class SportFieldStudent(models.Model):


#     student = models.ForeignKey(Student, on_delete=models.CASCADE,verbose_name='دانشجوی ورزشکار')
#     sportField = models.ForeignKey(SportField, on_delete=models.CASCADE,verbose_name='رشته ورزشی')
#     User_sport_video = models.ImageField(upload_to=upload_image_path, null=True, blank=True, verbose_name=' ویدیوی مسابقه  ')
#     sportFieldStudent_DateTime = models.DateTimeField(auto_now_add=True)


#     def jsportFieldStudent_dateTime(self):
#         return jalali_converter(self.sportFieldStudent_DateTime)
#     jsportFieldStudent_dateTime.short_description = "زمان ارسال ویدئو"

#     class Meta:
#         verbose_name_plural = 'جشنواره ورزشی'
#         verbose_name = ' جشنواره ورزشی '


#     def __str__(self):
#         return self.student.User_name + " " + self.student.User_family + " " + "از" + self.student.User_university.University_name


#     def save(self, *args, **kwargs):
#         numStu=SportFieldStudent.objects.filter(student=self.student).count()
#         numsport=SportFieldStudent.objects.filter(student=self.student,sportField=self.sportField).first()
#         if not numsport and numStu<=1:
#             print(f'student is :{self.student}')
#             print(f'numstu is :{numStu}')
#             super().save(*args, **kwargs)  # Call the "real" save() method.
#         else:
#             raise RuntimeError


# class Result(models.Model):
#     sportFieldStudent = models.OneToOneField(SportFieldStudent, on_delete=models.CASCADE,verbose_name=' دانشجوی ورزشکار ')
#     Result_reg_DateTime = models.DateTimeField(verbose_name='تاریخ ثبت نتیجه',auto_now_add=True)
#     Result_num = models.IntegerField(verbose_name='نتیجه',validators=[MinValueValidator(1), MaxValueValidator(100)])

#     class Meta:
#         verbose_name_plural = 'ثبت نتایج  '
#         verbose_name = '  نتیجه'
#     def __str__(self):
#         return self.sportFieldStudent.student.User_name + " " + self.sportFieldStudent.student.User_family + " " + "از" + self.sportFieldStudent.student.User_university.University_name +" در "+self.sportFieldStudent.sportField.SportField_name


#     def jResult_reg_dateTime(self):
# 	    return jalali_converter(self.Result_reg_DateTime)
#     jResult_reg_dateTime.short_description = "زمان  ثبت نمره"


# class Result_obj(models.Model):
#     result = models.OneToOneField(Result,on_delete=models.CASCADE,verbose_name='نمره اولیه فرد')
#     Result_obj_num = models.IntegerField(null=True,verbose_name=' امتیاز بعد از بازبینی',
#     validators=[MinValueValidator(1), MaxValueValidator(100)])
#     Result_obj_DateTime = models.DateTimeField(verbose_name='تاریخ ثبت اعتراض',null=True,blank=True,auto_now_add=True)
#     # usr= models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='نام وارد کننده اطلاعات',editable=False)

#     # def clean(self):
#     #     numsResult=Result_obj.objects.filter(result=self.result).count()
#     #     if numsResult>1 :
#     #         raise RuntimeError
#     #     else:
#     #         pass

#             # raise django_excetions.ValidationError('Measurement is outside the run')

#     # def save(self, *args, **kwargs):
#     #     # numStu=SportFieldStudent.objects.filter(student=self.student).count()

#     #     numsResult=Result_obj.objects.filter(result=self.result).count()
#     #     if numsResult<=1 :
#     #         print(f'numsResult is :{numsResult}')
#     #         super().save(*args, **kwargs)  # Call the "real" save() method.
#     #     else:
#     #         return RuntimeError
#     class Meta:
#         verbose_name_plural = 'ثبت  اعتراضات '
#         verbose_name = ' اعتراض '
#     def __str__(self):
#         return self.result.sportFieldStudent.student.User_name + " " + self.result.sportFieldStudent.student.User_family + " " + "از" + self.result.sportFieldStudent.student.User_university.University_name +" در "+self.result.sportFieldStudent.sportField.SportField_name+" با نمره اولیه "+str(self.result.Result_num)


#     def jResult_obj_dateTime(self):
# 	    return jalali_converter(self.Result_obj_DateTime)
#     jResult_obj_dateTime.short_description = "زمان  ثبت نتیجه اعتراض"
