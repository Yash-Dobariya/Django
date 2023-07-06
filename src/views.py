from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from src.models import User
from src.utils.serializer import get_user, get_all_user, update_user, soft_delete_user
import json
from src.utils.bearer_token import (
    create_access_token,
    create_refresh_token,
    token_required,
)


@csrf_exempt
def sign_up(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user = User.objects.create(
            first_name=data.get("first_name"),
            last_name=data.get("last_name"),
            email_id=data.get("email_id"),
            password=data.get("password"),
            mobile_no=data.get("mobile_no"),
            address=data.get("address"),
        )
        return get_user(user, status=201)


@csrf_exempt
def login(request):
    if request.method == "POST":
        login_data = json.loads(request.body)
        email_id = login_data.get("email_id")
        password = login_data.get("password")
        user = User.objects.filter(email_id=email_id, password=password).first()

        if user:
            access_token = (
                create_access_token(
                    subject={
                        "id": str(user.id),
                        "email_id": user.email_id,
                        "first_name": user.first_name,
                        "last_name": user.last_name,
                    },
                ),
            )
            refresh_token = (
                create_refresh_token(
                    subject={
                        "id": str(user.id),
                        "email_id": user.email_id,
                        "first_name": user.first_name,
                        "last_name": user.last_name,
                    }
                ),
            )

            return JsonResponse(
                {"access_token": access_token, "refresh_token": refresh_token}
            )
        else:
            return JsonResponse({"message": "wrong email_id and password!!!"})


@token_required
@csrf_exempt
def get_particular_user(request, id):
    if request.method == "GET":
        user = User.objects.filter(id=id).first()
        if not user:
            return JsonResponse({"message": "Id is not valid"}, status=404)
        return get_user(user, status=200)


@token_required
@csrf_exempt
def all_users(request):
    if request.method == "GET":
        users = User.objects.all()
        return get_all_user(users)


@token_required
@csrf_exempt
def updating_user(request, id):
    if request.method == "PUT":
        user = User.objects.filter(id=id).first()
        if not user:
            return JsonResponse({"message": "Id is not valid"}, status=404)

        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"message": "Invalid JSON data"}, status=400)

        return update_user(user, data, request)
    else:
        return JsonResponse({"message": "Invalid request method"}, status=405)


@token_required
@csrf_exempt
def deleting_user(request, id):
    if request.method == "DELETE":
        user = User.objects.filter(id=id).first()
        if not user:
            return JsonResponse({"message": "Id is not valid"}, status=404)

        return soft_delete_user(user)
    else:
        return JsonResponse({"message": "Invalid request method"}, status=405)
