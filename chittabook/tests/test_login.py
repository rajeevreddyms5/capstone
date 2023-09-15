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
    
    #test login page by name
    def test_template_name_correct(self):  
        response = self.client.get(reverse("account_login"))
        self.assertEqual(response.status_code, 200)  
    
    # test login page template name
    def test_template_name_correct(self):  
        response = self.client.get(reverse("account_login"))
        self.assertTemplateUsed(response, "account/login.html")

    # test login page content
    def test_template_content(self):
        response = self.client.get("/accounts/login/")
        self.assertContains(response, '<p>Welcome Back! Change your relationship with money. This platform is designed to empower you to make informed financial decisions, develop healthy spending habits, and achieve your financial goals.</p>')
        self.assertContains(response, '<h1 class="text-center"')
        self.assertNotContains(response, "Not on the page")

    # test login page functionality by login
    def test_login_page_functionality(self):
        self.assertTrue(self.client.login(email="normal@user.com", password="foo"))
        response = self.client.post("/accounts/login/", {
            "email": "normal@user.com",
            "password": "foo"
        })
        self.assertRedirects(response, "/home", target_status_code=301)

        
    