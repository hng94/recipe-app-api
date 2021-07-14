from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        # Test create email
        email = "hoang@dev.com"
        password = "Pastwork123"
        user = get_user_model().objects.create_user(email=email, password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        # Test normalized email
        email = "test@DEV.com"
        user = get_user_model().objects.create_user(email, "test123")
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        # Test invalid email
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "test123")

    def test_create_new_superuser(self):
        # test creating new superuser
        user = get_user_model().objects.create_superuser(
            "test@dev.com",
            "test123"
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)