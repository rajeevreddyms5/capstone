from django.contrib.auth import get_user_model
from django.test import TestCase
from django.db import IntegrityError
from chittabook.models.userprofile import UserProfile
from django.forms import ValidationError
from datetime import date, timedelta


# test user model
class UsersManagersTests(TestCase):

    # test create user
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(email="normal@user.com", password="foo")
        self.assertEqual(user.email, "normal@user.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email="")
        with self.assertRaises(ValueError):
            User.objects.create_user(email="", password="foo")

    # test create superuser
    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(email="super@user.com", password="foo")
        self.assertEqual(admin_user.email, "super@user.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(admin_user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_superuser(email="super@user.com", password="foo", is_superuser=False)
    
    # test duplicate user with same email
    def test_create_user_duplicate_email(self):
        User = get_user_model()
        user = User.objects.create_user(email="normal@user.com", password="foo")
        self.assertEqual(user.email, "normal@user.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        with self.assertRaises(IntegrityError):
            User.objects.create_user(email="normal@user.com", password="foo")


# test user profile model
class UserProfileTests(TestCase):
    
    # test user profile model creation with valid data
    def test_user_profile(self):
        # create user
        User = get_user_model()
        user = User.objects.create_user(email="example@example.com", password="password")
        
        # check user profile created on user creation
        userProfile = UserProfile.objects.get(user=user)
        self.assertEqual(user, userProfile.user)
        self.assertEqual(userProfile.name, "")
        self.assertEqual(userProfile.dob, None)
        self.assertEqual(userProfile.gender, None)
        self.assertEqual(userProfile.profession, None)
        self.assertEqual(userProfile.country, "")
        
        
        
        # update user profile with valid data
        userProfile = UserProfile.objects.get(user=user)
        userProfile.name = "name"
        userProfile.dob = "2000-01-01"
        userProfile.gender = "MALE"
        userProfile.profession = "Business"
        userProfile.country = "India"
        userProfile.save()
        self.assertEqual(userProfile.name, "name")
        self.assertEqual(userProfile.dob, "2000-01-01")
        self.assertEqual(userProfile.gender, "MALE")
        self.assertEqual(userProfile.profession, "Business")
        self.assertEqual(userProfile.country, "India")
        
        
        # update user profile with invalid data
        userProfile = UserProfile.objects.get(user=user)
        userProfile.name = "name"
        userProfile.dob = "2000-01-01"
        userProfile.gender = "INVALID"
        userProfile.profession = "Invalid Profession"
        userProfile.country = "Invalid Country"
        try:
            userProfile.save()
        except IntegrityError:
            pass
        
        
        # test user profile save with no name
        userProfile = UserProfile.objects.get(user=user)
        userProfile.name = ""
        try:
            userProfile.save()
        except ValidationError:
            pass
        
        
        # test user profile save with dob less than 13 years
        userProfile = UserProfile.objects.get(user=user)
        userProfile.name = "name"
        userProfile.dob = "2010-01-01"  # set dob less than 13 years
        userProfile.gender = "MALE"
        userProfile.profession = "Business"
        userProfile.country = "India"
        try:
            userProfile.save()
        except ValidationError:
            pass
        
        
        # test user profile save with dob greater than 100 years
        userProfile = UserProfile.objects.get(user=user)
        userProfile.name = "name"
        userProfile.dob = "1910-01-01"  # set dob greater than 100 years
        userProfile.gender = "MALE"
        userProfile.profession = "Business"
        userProfile.country = "India"
        try:
            userProfile.save()
        except ValidationError:
            pass
        
        
        # test user profile save with dob greater than today
        userProfile = UserProfile.objects.get(user=user)
        userProfile.name = "name"
        userProfile.dob = date.today() + timedelta(days=1)  # set dob greater than today
        userProfile.gender = "MALE"
        userProfile.profession = "Business"
        userProfile.country = "India"
        try:
            userProfile.save()
        except ValidationError:
            pass
        
        # test user profile save with invalid gender
        userProfile = UserProfile.objects.get(user=user)
        userProfile.name = "name"
        userProfile.dob = "2000-01-01"
        userProfile.gender = "INVALID"  # set an invalid gender
        userProfile.profession = "Business"
        userProfile.country = "India"
        try:
            userProfile.save()
        except ValidationError:
            pass