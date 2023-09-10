from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

# test case for login page
class LoginTests(TestCase):
    
    def setUp(self):
        User = get_user_model()
        user = User.objects.create_user(email="normal@user.com", password="foo")
    
    # test login page
    def test_login_page_status_code(self):
        response = self.client.get("/accounts/login/")
        self.assertEqual(response.status_code, 200)
    
    # test login page by name
    def test_template_name_correct(self):  
        response = self.client.get("/accounts/login/")
        self.assertTemplateUsed(response, "accounts/login.html")  
    
    def test_template_content(self):
        response = self.client.get("/accounts/login/")
        self.assertContains(response, "<h1>Log In</h1>")
        self.assertNotContains(response, "Not on the page")
        
    