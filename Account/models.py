from tkinter import CASCADE
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _
from Utils.general_model import GeneralModel
from .MyUserManager import MyUserManager
from django.contrib.auth.models import User, AbstractUser

# Create your models here.


class MyUser(AbstractUser):

    objects= MyUserManager()
    backend = 'Account.MyBackend.MobileBackend'


    User_national_code = models.CharField(
        max_length=10, verbose_name='کد ملی ', unique=True)
    User_mobile = models.CharField(
        max_length=11, verbose_name='شماره موبایل', unique=True)
    password = models.CharField(verbose_name='پسورد ', max_length=128)

    REQUIRED_FIELDS = ['User_national_code']
    username = None
    USERNAME_FIELD = 'User_mobile'
    class Meta:
        verbose_name_plural = 'کاربران '
        verbose_name = 'کاربر '
        ordering = ['-first_name']

    def __str__(self):
        
        # return self.first_name + " " + self.last_name
        return self.User_national_code



User = get_user_model()


class ActivationCode(GeneralModel):

    TYPE_CHOICES = (
        ('REGISTER', 'REGISTER'),
        ('FORGET', 'FORGET'),
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=_('Activation Code'),
    )
    type = models.CharField(
        max_length=128,
        choices=TYPE_CHOICES,
        verbose_name=_('Type'),
    )
    code = models.CharField(
        max_length=32,
        verbose_name=_('Code'),
    )
    retry = models.PositiveSmallIntegerField(
        verbose_name=_('Retry'),
        default=0,
    )
    used = models.BooleanField(
        default=False,
        verbose_name=_('Used'),
    )

    class Meta:
        verbose_name = _('ActivationCode')
        verbose_name_plural = _('ActivationCodes')

    def __str__(self):
        return f'{self.code} As {self.TYPE_CHOICES} code send in date{self.create_at}'




# @deconstructible
# class UnicodeUsernameValidator(validators.RegexValidator):
#     regex = r"^[\w.@+-]+\Z"

#     message = _(
#         "Enter a valid username. This value may contain only letters, "
#         "numbers, and @/./+/-/_ characters."
#     )
#     flags = 0



    # username_validator = UnicodeUsernameValidator()
    # username = models.CharField(
    #     _("username"),
    #     max_length=150,
    #     unique=True,

    #     help_text=_(
    #         "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
    #     ),
    #     validators=[username_validator],
    #     error_messages={
    #         "unique": _("A user with that username already exists."),
    #     },
    # )
    # gender = models.PositiveSmallIntegerField(
    #     choices=GENDER_CHOICES, null=True, blank=True, verbose_name='جنسیت')
    # User_personal_Img = models.ImageField(
    #     upload_to=upload_image_path, null=True, blank=True, verbose_name='عکس پرسنلی  ')

    # hits = models.ManyToManyField(SportField, through="SportFieldStudent", blank=True, related_name='hits', verbose_name='بازدیدها')

    # def thumbnail_tag(self):
    #     if self.User_personal_Img:
    #         return format_html("<img width=60 height=60 style='border-radius: 5px;' src='{}'>".format(self.User_personal_Img.url))
    #     else:
    #         return format_html("<img width=60 height=60 style='border-radius: 5px' src='{}'>".format('..\..\..\media\custom_login\imgStu\default.png'))
    # thumbnail_tag.short_description = "تصویر کاربر"

    # def jUser_reg_dateTime(self):
    #     return jalali_converter(self.date_joined)
    # jUser_reg_dateTime.short_description = "زمان  ثبت نام"
