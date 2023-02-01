"""
Test for django models.
"""
from decimal import Decimal

from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


class ModelTests(TestCase):
    """Test for django models."""

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful."""
        email = 'test@example.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized."""
        sample_emails = [['test1@EXAMPLE.com', 'test1@example.com'],
                         ['Test2@Example.com', 'Test2@example.com'],
                         ['TEST3@EXAMPLE.com', "TEST3@example.com"],
                         ['test4@example.COM', 'test4@example.com'],
                         ]
        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(
                email=email,
                password='testpass123',
            )
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_error(self):
        """Test creating user without email raises value error."""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'testpass123')

    def test_create_new_superuser(self):
        """Test creating a new superuser."""
        user = get_user_model().objects.create_superuser(
            'test@example.com',
            'testpass123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_create_recipe(self):
        """Test creating a recipe."""
        user = get_user_model().objects.create_user(
            'test@example.com',
            'testpass123'
        )
        recipe = models.Recipe.objects.create(
            user=user,
            title='Test recipe',
            time_minutes=5,
            price=Decimal('5.00'),
            description='Test description',
        )

        self.assertEqual(str(recipe), recipe.title)

    def test_create_irradiation(self):
        """Test creating a irradiation."""
        user = get_user_model().objects.create_user(
            'test@example.com',
            'testpass123'
        )
        irradiation = models.Irradiation.objects.create(
            user=user,
            id=1,
            country='Test country',
            latitude=5.00,
            longitude=5.00,
            annual=5.00,
            january=5.00,
            february=5.00,
            march=5.00,
            april=5.00,
            may=5.00,
            june=5.00,
            july=5.00,
            august=5.00,
            september=5.00,
            october=5.00,
            november=5.00,
            december=5.00,
        )
        self.assertEqual(str(irradiation), str(irradiation.id))
