import json
from django.conf import settings

redis_instance = settings.REDIS_INSTANCE


def retrieve_user_data(session_id):
    """ Retrieve user data """
    return json.loads(redis_instance.get(session_id))


def get_user_level(session_id):
    """ Retrieve user level """
    user_data = retrieve_user_data(session_id)
    return user_data['level']
