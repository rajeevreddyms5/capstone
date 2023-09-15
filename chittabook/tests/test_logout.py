from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

# test case for login page
class LoginTests(TestCase):
    
    def setUp(self):
        User = get_user_model()
        user = User.objects.create_user(email="normal@user.com", password="foo")
    

    # test logout page
    def test_logout_functionality(self):
        self.assertTrue(self.client.login(email="normal@user.com", password="foo"))
        response = self.client.post("/accounts/login/", {
            "email": "normal@user.com",
            "password": "foo"
        })
        self.assertRedirects(response, "/home", target_status_code=301)
