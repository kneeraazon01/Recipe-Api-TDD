from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):
    """ This tests the creating user with the user email successfully"""

    def test_create_user_with_email_successful(self):
        email = "test@gmail.com"
        password = "test123"
        user = get_user_model().objects.create_user(email=email, password=password)
        self.assertEquals(user.email, email)
        self.assertTrue(user.check_password(password))
        # ? thats is because the password will be encrypted

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = "test@GMAIl.com"
        user = get_user_model().objects.create_user(email, "test123")

        self.assertEqual(user.email, email.lower())
