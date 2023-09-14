from django.core import mail
from django.test import TestCase

# Create your tests here.
class EmailTest(TestCase):
    def test_send_mail(self):
        mail.send_mail(
            'Hi there',
            'Welcome to chittabook.',
            'services.chittabook@gmail.com',
            ['user@gmail.com'],
            fail_silently=False
        )

        # Test that one message has been sent
        self.assertEqual(len(mail.outbox), 1)

        # Test that the message has the correct subject
        self.assertEqual(mail.outbox[0].subject, 'Hi there')