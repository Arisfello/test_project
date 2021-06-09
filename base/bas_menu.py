from django.conf import settings
from django.http import HttpResponse
from ussd.models import UssdLog
from ussd.redis_tracker.redis_db import get_user_level
from django.conf import settings
from datetime import datetime
from pytz import timezone
import json


class Menu(object):
    def __init__(self, session_id, session, user_response, phone_number=None, level=None):
        self.session = session
        self.session_id = session_id
        self.user_response = user_response
        self.phone_number = phone_number
        self.level = level
