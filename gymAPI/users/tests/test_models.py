from decimal import Decimal
from users.models import User, Profile
from users.tests.test_setup import TestSetUp
from django.core.files.uploadedfile import SimpleUploadedFile
from django.db import IntegrityError

class TestUSerModel(TestSetUp):

    def test_create_user(self):
        user = User.objects.create_user(
            name="Jhon Adam",
            email= self.user_data['email'], 
            username= self.user_data['username'],
            password=self.user_data['password']
        )
        self.assertIsInstance(user, User)
        self.assertEqual(user.is_verified, False) 
        self.assertEqual(user.is_superuser, False) 
        self.assertEqual(user.is_staff, False) 
        self.assertEqual(user.is_active, True) 
        self.assertEqual(user.name, "Jhon Adam") 
        self.assertEqual(user.email, self.user_data['email']) 
        self.assertEqual(user.username, self.user_data['username']) 

    def test_create_user_riases_error_when_no_usename_provided(self):
        self.assertRaises(
                        ValueError,
                        User.objects.create_user,
                        username="",
                        name="Jhon Adam",
                        email= self.user_data['email'], 
                        password=self.user_data['password']
                    )
   
    def test_create_user_riases_error_when_no_email_provided(self):
        self.assertRaises(
                        ValueError,
                        User.objects.create_user,
                        username=self.user_data['username'],
                        name="Jhon Adam",
                        email= "", 
                        password=self.user_data['password']
                    )
    def test_create_user_riases_error_when_no_name_provided(self):
        self.assertRaises(
                        ValueError,
                        User.objects.create_user,
                        username=self.user_data['username'],
                        name="",
                        email=self.user_data['email'], 
                        password=self.user_data['password']
                    )
    def test_create_user_riases_error_when_no_password_provided(self):
        self.assertRaises(
                        ValueError,
                        User.objects.create_user,
                        username=self.user_data['username'],
                        name="Jhon Wick",
                        email=self.user_data['email'], 
                        password=""
                    )
    def test_create_super_user(self):
        user = User.objects.create_superuser(
            name="Jhon Adam",
            email= self.user_data['email'], 
            username= self.user_data['username'],
            password=self.user_data['password']
        )
        self.assertIsInstance(user, User)
        self.assertEqual(user.is_verified, False) 
        self.assertEqual(user.is_superuser, True) 
        self.assertEqual(user.is_staff, True) 
        self.assertEqual(user.is_active, True) 
        self.assertEqual(user.name, "Jhon Adam") 
        self.assertEqual(user.email, self.user_data['email']) 
        self.assertEqual(user.username, self.user_data['username']) 
    
    def test_create_superuser_riases_error_when_no_usename_provided(self):
        self.assertRaises(
                        ValueError,
                        User.objects.create_superuser,
                        username="",
                        name="Jhon Adam",
                        email= self.user_data['email'], 
                        password=self.user_data['password']
                    )
   
    def test_create_superuser_riases_error_when_no_email_provided(self):
        self.assertRaises(
                        ValueError,
                        User.objects.create_superuser,
                        username=self.user_data['username'],
                        name="Jhon Adam",
                        email= "", 
                        password=self.user_data['password']
                    )
    def test_create_superuser_riases_error_when_no_name_provided(self):
        self.assertRaises(
                        ValueError,
                        User.objects.create_superuser,
                        username=self.user_data['username'],
                        name="",
                        email=self.user_data['email'], 
                        password=self.user_data['password']
                    )
    def test_create_superuser_riases_error_when_no_password_provided(self):
        self.assertRaises(
                        ValueError,
                        User.objects.create_superuser,
                        username=self.user_data['username'],
                        name="Jhon Wick",
                        email=self.user_data['email'], 
                        password=""
                    )

    def test_token_method_returns_refresh_and_access_token(self):
        user = User.objects.create_superuser(
            name="Jhon Adam",
            email= self.user_data['email'], 
            username= self.user_data['username'],
            password=self.user_data['password']
        )
        tokens = user.tokens()

        self.assertIsInstance(tokens, dict)
        self.assertTrue(tokens['refresh'])
        self.assertTrue(tokens['access'])

class TestProfileModel(TestSetUp):
    def test_create_profile(self):
        user = User.objects.create_user(
            name="Jhon Adam",
            email= self.user_data['email'], 
            username= self.user_data['username'],
            password=self.user_data['password']
        )
        profile = Profile.objects.create(
            user=user,
            phone="+01155217475",
            age=21,
            weight=85,
            height=172,
            image=SimpleUploadedFile(
                        name='test_image.jpg',
                        content=open("media/users/images/default-avatar.png", 'rb').read(), 
                        content_type='image/jpeg'),
            gender='Male',
        )
        bmi_value = profile.weight / Decimal(((profile.height / 100)**2))
        self.assertIsInstance(profile, Profile)
        self.assertEqual(profile.bmi, bmi_value)

    def test_raises_error_when_creates_profile_for_user_with_profile(self):
        user = User.objects.create_user(
            name="Jhon Adam",
            email= self.user_data['email'], 
            username= self.user_data['username'],
            password=self.user_data['password']
        )
        profile = Profile.objects.create(
            user=user,
            phone="+01155217475",
            age=21,
            weight=85,
            height=172,
            image=SimpleUploadedFile(
                        name='test_image.jpg',
                        content=open("media/users/images/default-avatar.png", 'rb').read(), 
                        content_type='image/jpeg'),
            gender='Male',
        )
        self.assertRaises(
                        IntegrityError,
                        Profile.objects.create,
                        user=user,
                        phone="+01155217475",
                        age=21,
                        weight=85,
                        height=172,
                        image=SimpleUploadedFile(
                                    name='test_image.jpg',
                                    content=open("media/users/images/default-avatar.png", 'rb').read(), 
                                    content_type='image/jpeg'),
                        gender='Male')
