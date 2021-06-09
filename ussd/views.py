from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from ussd.redis_tracker.redis_db import get_user_level
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Users, Register_user, reg_user


trying = Register_user
response = ''
# print(Register_user)


@csrf_exempt
def index(request):
    global response
    if request.method == 'POST' 'GET':
        params = request.POST
        session_id = params.get('sessionId', None)
        service_code = params.get('serviceCode', None)
        phone_number = params.get('phoneNumber', None)
        text = params.get('text', 'default')
        textValue = text.split('*')
        level = get_user_level(session_id)

        if text == '':
            response = "CON Welcome to the National Addressing System \n"
            response += "1. Register an account \n"
            response += "2. My Account"

        elif text == '1':
            response = "CON Who do you want to register for? \n"
            response += "1. Your Account \n"
            response += "2. Someone Else"

        elif text == '1*1':
            response = "CON Please enter your Name"

        elif textValue[0] == 1 and textValue[1] == 1 and level == 3:
            response = "CON Please enter your Gender"

        elif textValue[0] == 1 and textValue[1] == 1 and level == 4:
            response = "CON Please enter your Email"

        elif textValue[0] == 1 and textValue[1] == 1 and level == 5:
            response = "End Your data has been captured successfully! Thank you for registering on the National " \
                       "Addressing System "

        elif text == '1*2':
            response = "CON Please enter the Name of the person you want to register for"

        elif textValue[0] == 1 and textValue[1] == 2 and level == 3:
            response = "CON Please enter their Gender"

        elif textValue[0] == 1 and textValue[1] == 2 and level == 4:
            response = "CON Please enter their Email"

        elif textValue[0] == 1 and textValue[1] == 2 and level == 5:
            response = "End Their data has been captured successfully! Thank you for registering on the National " \
                       "Addressing System "

    return HttpResponse(response)


def user_is_starting(text):
    if len(text) > 0:
        return False
    else:
        return True


@api_view(['GET'])
def get_user_detail(request):
    phone_number = request.query_params.get('phone_number', None)
    return Response
