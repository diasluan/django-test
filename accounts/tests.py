from django.test import TestCase
from django.contrib.auth import get_user_model


class UserAccountTests(TestCase):
    def test_new_adminuser(self):
        db = get_user_model()
        admin_user = db.objects.create_admin(
            "admin@test.com", "admin_name", "admin_password"
        )
        self.assertEqual(admin_user.email, "admin@test.com")
        self.assertEqual(admin_user.name, "admin_name")
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_active)
        self.assertEqual(str(admin_user), "<User name=admin_name email=admin@test.com>")

        with self.assertRaises(ValueError):
            db.objects.create_admin(
                email="admin@test.com",
                name="admin_name",
                password="password",
                is_staff=False,
            )

        with self.assertRaises(ValueError):
            db.objects.create_admin(
                email="", name="admin_name", password="password", is_staff=True
            )

    def test_new_user(self):
        db = get_user_model()
        user = db.objects.create_user("user@test.com", "name", "password")
        self.assertEqual(user.email, "user@test.com")
        self.assertEqual(user.name, "name")
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_active)

        with self.assertRaises(ValueError):
            db.objects.create_user(email="", name="name", password="password")
