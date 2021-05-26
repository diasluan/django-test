from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Timezone


class TimezoneTests(TestCase):
    def test_new_timezone(self):
        User = get_user_model()
        user = User.objects.create_admin(
            "admin@test.com", "admin_name", "admin_password"
        )
        tz = Timezone.objects.create(
            name="test_name", city="test_city", gmt_diff=-93.0, owner=user
        )

        self.assertEqual(tz.name, "test_name")
        self.assertEqual(tz.city, "test_city")
        self.assertEqual(tz.gmt_diff, -3)
        self.assertEqual(tz.owner, user)
        self.assertEqual(tz.get_gmt_repr(), "-03:00")
        self.assertEqual(str(tz), "<Timezone: test_name @ test_city is -03:00>")
