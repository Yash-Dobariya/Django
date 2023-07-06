from tests.utils.functions import id_for


EXPECTED_DATA = [
    {
        "access_token": {
            "id": id_for("id_1"),
            "first_name": "Adc",
            "last_name": "Acd",
            "email_id": "abc@gmail.com",
        },
    },
    {
        "get_particular_user": {
            "id": id_for("id_1"),
            "first_name": "Adc",
            "last_name": "Acd",
            "email_id": "abc@gmail.com",
            "mobile_no": 689632145,
            "address": "India",
        },
    },
]
