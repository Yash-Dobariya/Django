from django.test import TestCase
from src.models import User
from django.test import Client
from django.urls import reverse
from tests.utils.seed_data import SEED_DATA
from tests.utils.expected_data import EXPECTED_DATA
from src.utils.bearer_token import create_access_token
from tests.utils.functions import id_for


class UserTestCase(TestCase):
    """User testcases"""

    client = Client()
    User.objects.create(
        id=id_for("id_1"),
        first_name="Adc",
        last_name="Acd",
        email_id="aadcac",
        mobile_no=689632145,
        address="Adca",
    )

    def test_sign_up_user(self):
        """testcase user sign_up"""

        response = self.client.post(
            reverse("sign_up"),
            data=SEED_DATA[0]["sign_up"],
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 201)
        self.assertTrue(User.objects.filter(first_name="demo").first())
        self.assertTrue(User.objects.filter(last_name="demo").first())
        self.assertTrue(User.objects.filter(password="demo").first())
        self.assertTrue(User.objects.filter(email_id="demo").first())
        self.assertTrue(User.objects.filter(mobile_no=789654).first())
        self.assertTrue(User.objects.filter(address="demo").first())

    def test_login(self):
        """testcase user login"""

        response = self.client.post(
            reverse("login"),
            data=SEED_DATA[1]["login"],
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)

    def test_get_particular_user(self):
        """testcase user get particular user"""

        headers = {
            "Authorization": f"Bearer {create_access_token(EXPECTED_DATA[0]['access_token'])}"
        }
        response = self.client.get(
            reverse("particular_user", args=id_for("id_1").split(','),), headers=headers
        )
        breakpoint()
        self.assertEqual(response.status_code, 200)

        self.assertEqual(response.json(), EXPECTED_DATA[1]["get_particular_user"])
