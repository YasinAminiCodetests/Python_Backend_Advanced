from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_email_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email="yasinyahoo"
        password="Yas123"

        user=get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))
    
    def test_normilzing_email(self):
        """checks if the email is normalize"""
        email="yasin@YAHOO.CoM"
        password="Yas123"
        user=get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email.lower())

    def test_email_validation(self):
        """check if the email exits"""
        """This model is not working for other than NONE values"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None,'Yasin123')

    def test_create_Superuser(self):
        """Ccreating the supper user"""
        user=get_user_model().objects.create_superuser(
            "Yasin@yahoo.com","1234"
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)