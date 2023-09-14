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
        response = self.client.get("/home/")

        # test homepage content
        self.assertContains(response, 'Sign Out')
        self.assertNotContains(response, "Not on the page")


        # test logout functionality
        response = self.client.post(path=reverse("account_logout"), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, reverse("index")) # logout redirects to index page


        # check whether logout is successful
        response = self.client.get("/home/")
        self.assertRedirects(response, "/accounts/login/?next=/home/", target_status_code=200)


