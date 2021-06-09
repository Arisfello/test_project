from django.db import models

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


def is_user_registered(phone):
    user = Users.objects.get(phone=phone)

    if user.is_registration_done == 0:
        return False
    else:
        return True


class Users(models.Model):
    phone = models.CharField(max_length=255)
    name = models.CharField(max_length=255, null=True)
    gender = models.SmallIntegerField(default=0)
    email = models.EmailField(max_length=254, null=True)
    session = models.IntegerField(default=0)
    session_id = models.CharField(max_length=255, null=True)
    progress = models.CharField(max_length=100, default=0)
    selection_menu = models.CharField(max_length=100, null=True, blank=True)
    confirm_from = models.IntegerField(default=0)
    menu_id = models.IntegerField(default=0)
    menu_item_id = models.IntegerField(default=0)
    access_count = models.IntegerField(default=0)
    is_registration_done = models.IntegerField(default=0)
    short_code = models.CharField(max_length=100, default=0)
    created_date = models.DateTimeField(default=timezone.now)

    def count_access(self):
        self.access_count += 1

    def __str__(self):
        return self.phone

    class Meta:
        verbose_name = "User Data"
        verbose_name_plural = "Users Data"


class UssdLog(models.Model):
    session_id = models.CharField(primary_key=True, max_length=250)
    phone_number = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.session_id} - {self.phone_number} - {self.created_at}"

    class Meta:
        verbose_name = "User Log"
        verbose_name_plural = "Users Logs"


class Register_user:
    def __init__(self, get_name, get_email, get_gender):
        self.email = get_email
        self.name = get_name
        self.gender = get_gender

    def display_user(self):
        print(self.name, self.gender, self.email)


reg_user = Register_user('input()', 'input()', 'input()')
