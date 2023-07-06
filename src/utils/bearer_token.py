from functools import wraps
from datetime import datetime, timedelta
from django.http import JsonResponse
from src.config import Config
import jwt


def create_access_token(subject: dict, expiry_time: timedelta = timedelta(days=1)):
    """create access token"""

    if expiry_time:
        expiry_time = datetime.utcnow() + expiry_time
    data = {**subject, "exp": expiry_time}
    return jwt.encode(payload=data, key=Config.JWT_SECRET_KEY, algorithm="HS256")


def create_refresh_token(subject: dict, expiry_time: timedelta = timedelta(days=7)):
    """create refresh token"""

    if expiry_time:
        expiry_time = datetime.utcnow() + expiry_time
    data = {**subject, "exp": expiry_time}
    return jwt.encode(payload=data, key=Config.JWT_SECRET_KEY, algorithm="HS256")


def token_required(view_func):
    """decode token and check token"""

    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        jwt_token = request.headers.get("Authorization").split()[1]

        if jwt_token:
            try:
                decode_jwt = jwt.decode(
                    jwt=jwt_token, key=Config.JWT_SECRET_KEY, algorithms=["HS256"]
                )

                if decode_jwt["exp"] <= datetime.timestamp(datetime.now()):
                    return JsonResponse({"message": "Token has expired!!!"})
                else:
                    request.user = {
                        "id": decode_jwt["id"],
                        "email_id": decode_jwt["email_id"],
                        "first_name": decode_jwt["first_name"],
                        "last_name": decode_jwt["last_name"],
                    }
            except jwt.InvalidTokenError:
                return JsonResponse({"message": "Invalid token!!!"})
        else:
            return JsonResponse({"message": "Token not found!!!"})

        return view_func(request, *args, **kwargs)

    return wrapper
