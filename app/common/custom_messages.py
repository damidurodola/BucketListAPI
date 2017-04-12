#!flask/bin/python3/

from flask_restful import abort, request

from app.models import BucketList, BucketListItem, User
from functools import wraps


class CustomMessages:
    # Custom errors for the Restful API is defined here.


    def sucess_message(message):
        # Custom error message for not acceptable requests

        response = {'status': 'OK', 'message': message}
        return response

    def not_acceptable(message):
        # Custom error message for not acceptable requests

        response = {'status': 'Not Acceptable', 'message': message}
        return response

    def bad_request(message):
        # Custom error message for bad requests

        response = {'status': 'Bad Request', 'message': message}
        return response

    def server_error(message):
        # Custom error message for bad requests

        response = {'status': 'Internal Server Error', 'message': message}
        return response
