from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

# test index page
class indexpageTests(TestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
    def test_url_available_by_name(self):  
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
    def test_template_name_correct(self):  
        response = self.client.get(reverse("index"))
        self.assertTemplateUsed(response, "chittabook/index.html")
    def test_template_content(self):
        response = self.client.get(reverse("index"))
        self.assertContains(response, "<p>Track your income and expenses effortlessly with our Personal Financial Management Software. Gain control over your finances and make informed decisions for a brighter financial future. Start today!  (It's Free!)</p>")
        self.assertNotContains(response, "Not on the page")
