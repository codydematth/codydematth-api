from rest_framework.exceptions import ValidationError
from rest_framework.status import HTTP_400_BAD_REQUEST

def response_data(status_code, message, data=None, success=True):
    response = {
        "status": status_code,
        "hasError": not success,
        "data": {
            "message": message
        }
    }
    if data is not None:
        response['data']['data'] = data
    return response

def validate_email( value):
        if not value:
            raise ValidationError(response_data( status_code= HTTP_400_BAD_REQUEST, message= "Email is required" , success=False))
        elif not "@" in value or not "." in value:
            raise ValidationError(response_data( status_code= HTTP_400_BAD_REQUEST, message= "Invalid email format", success= False))
        return value 