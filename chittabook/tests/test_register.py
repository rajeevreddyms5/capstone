from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


# test case for register page
class RegisterTests(TestCase):
    
    def setUp(self):
        User = get_user_model()
        user = User.objects.create_user(email="normal@user.com", password="foo")
    
    # test register page
    def test_login_page_status_code(self):
        response = self.client.get("/accounts/signup/")
        self.assertEqual(response.status_code, 200)
    
    #test register page by name
    def test_template_name_correct(self):  
        response = self.client.get(reverse("account_signup"))
        self.assertEqual(response.status_code, 200)  
    
    # test register page template name
    def test_template_name_correct(self):  
        response = self.client.get(reverse("account_signup"))
        self.assertTemplateUsed(response, "account/signup.html")

    # test register page content
    def test_template_content(self):
        response = self.client.get("/accounts/signup/")
        self.assertContains(response, 'Already have an account? Then please')
        self.assertContains(response, '<h1 class="text-center"')
        self.assertNotContains(response, "Not on the page")

    # test register page functionality
    def test_register_page_functionality(self):
        response = self.client.post("/accounts/signup/", {
            "email": "normal@user.com",
            "password1": "foo",
            "password2": "foo"
        })
        self.assertTrue(response, 200)
        # self.assertRedirects(response, reverse("index")) 
        self.assertEqual(get_user_model().objects.all().count(), 1)
        