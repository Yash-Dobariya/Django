from django.http import JsonResponse
from django.http import HttpResponse


def get_user(user, status):
    """get particular user"""

    if user.is_delete == False:
        return JsonResponse(
            {
                "id": str(user.id),
                "first_name": user.first_name,
                "last_name": user.last_name,
                "email_id": user.email_id,
                "mobile_no": user.mobile_no,
                "address": user.address,
            },
            status=status,
        )
    else:
        return JsonResponse({"message": "Id is not valid"}, status=404)


def get_all_user(users):
    """get all user"""

    result = []
    for user in users:
        if user.is_delete == False:
            result.append(
                {
                    "id": str(user.id),
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "password": user.password,
                    "email_id": user.email_id,
                    "mobile_no": user.mobile_no,
                    "address": user.address,
                },
            )
    return HttpResponse(result, status=200)


def update_user(user, data, request):
    """update user"""

    if data.get("first_name"):
        user.first_name = data.get("first_name")
    if data.get("last_name"):
        user.last_name = data.get("last_name")
    if data.get("email_id"):
        user.email_id = data.get("email_id")
    if data.get("mobile_no"):
        user.mobile_no = data.get("mobile_no")
    if data.get("address"):
        user.address = data.get("address")

    from datetime import datetime

    user.updated_at = datetime.utcnow()
    user.updated_by = request.user.get("id")
    user.save()

    return JsonResponse({"message": "User updated successfully"})


def soft_delete_user(user):
    """user delete"""

    user.is_delete = True
    user.save()

    return JsonResponse({"message": "User deleted successfully"})
