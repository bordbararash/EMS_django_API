from . import jalali
from django.utils import timezone
import os
import random
import string
# from django.db import models
# from django.contrib.auth.models import AbstractUser, User
# from extensions.utils import jalali_converter
# from django.utils.html import format_html
# from django.core.validators import MaxValueValidator, MinValueValidator
# from django.contrib  import auth


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    file_name = ''.join(random.choice(string.ascii_lowercase) for i in range(16))
    final_name = f"{file_name}{ext}"
    return f"static/Person/UsrImgs/{final_name}"


def persian_numbers_converter(mystr):
	numbers = {
		"0": "۰",
		"1": "۱",
		"2": "۲",
		"3": "۳",
		"4": "۴",
		"5": "۵",
		"6": "۶",
		"7": "۷",
		"8": "۸",
		"9": "۹",
	}

	for e, p in numbers.items():
		mystr = mystr.replace(e, p)

	return mystr

def jalali_converter(time):
	jmonths = ["فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور", "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند",]

	time = timezone.localtime(time)

	time_to_str = "{},{},{}".format(time.year, time.month,time.day)
	time_to_tuple = jalali.Gregorian(time_to_str).persian_tuple()

	time_to_list = list(time_to_tuple)

	for index, month in enumerate(jmonths):
		if time_to_list[1] == index + 1:
			time_to_list[1] = month
			break

	output = "{} {} {}، ساعت {}:{}".format(
		time_to_list[2],
		time_to_list[1],
		time_to_list[0],
		time.hour,
		time.minute,
	)

	return persian_numbers_converter(output)