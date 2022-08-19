from rest_framework.test import APITestCase
from faker import Faker

    
class TestSetUp(APITestCase):

    def setUp(self):
        
        self.fake = Faker()
        
        username = self.fake.email().split('@')[0] + self.fake.email().split('@')[1]
        self.user_data = {
            "name": "user name",
            'email': self.fake.email(),
            'username': username,
            'password': "12345678910",
            'password_confirmation': "12345678910",
        }

        return super().setUp()

    def tearDown(self):
        return super().tearDown()