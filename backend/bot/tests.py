from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import BotMessage

class BotMessageModelTest(TestCase):
    def test_create_message(self):
        user = get_user_model().objects.create(username='test')
        msg = BotMessage.objects.create(user=user, text='hello')
        self.assertEqual(str(msg), f'{user}: hello')
