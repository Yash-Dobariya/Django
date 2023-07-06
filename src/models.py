from django.db import models

import uuid
from src.utils.same_model import DBmodel


class User(DBmodel):

    """User model"""

    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email_id = models.EmailField()
    mobile_no = models.IntegerField()
    address = models.CharField(max_length=255)

    class Meta:
        app_label = "src"
        db_table = "user"
