from users.tests.test_setup import TestSetUp
from users.models import User, Profile
from rest_framework_simplejwt.tokens import RefreshToken
import jwt
from django.core.files.uploadedfile import SimpleUploadedFile


class TestUserViewSet(TestSetUp):
    def test_user_cannot_register_with_no_data(self):
        res = self.client.post("/api/users/register/")
        self.assertEqual(res.status_code, 400)
    
    def test_user_can_register(self):
        
        res = self.client.post("/api/users/register/", self.user_data)   

        self.assertEqual(res.status_code, 201)
        self.assertEqual(res.data['username'], self.user_data["username"])
        self.assertEqual(res.data['name'], self.user_data["name"])
        self.assertEqual(res.data['email'], self.user_data["email"])

    def test_cannot_register_with_different_passwords(self):
        self.user_data["password_confirmation"] = "98765432100"
        res = self.client.post("/api/users/register/", self.user_data)   
        self.assertEqual(res.status_code, 400)

    def test_user_cannot_register_with_no_username(self):
        self.user_data["username"] = ""
        res = self.client.post("/api/users/register/", self.user_data)   
        self.assertEqual(res.status_code, 400)
    
    def test_user_cannot_register_with_no_name(self):
        self.user_data["name"] = ""
        res = self.client.post("/api/users/register/", self.user_data)   
        self.assertEqual(res.status_code, 400)

    def test_user_cannot_register_with_no_password(self):
        self.user_data["password"] = ""
        res = self.client.post("/api/users/register/", self.user_data)   
        self.assertEqual(res.status_code, 400)

    def test_user_cannot_register_with_no_email(self):
        self.user_data["email"] = ""
        res = self.client.post("/api/users/register/", self.user_data)   
        self.assertEqual(res.status_code, 400)

    def test_user_can_activate_email(self):
        user = User.objects.create_user(
            name="Jhon Adam",
            email= self.user_data['email'], 
            username= self.user_data['username'],
            password=self.user_data['password']
        )
        token = RefreshToken.for_user(user).access_token
        
        res = self.client.get(f"/api/users/verify-email/?token={token}")   
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data["email"], 'Email Successfully Activated')
        
        user = User.objects.get(username=self.user_data['username'])
        self.assertEqual(user.is_verified, True)

    def test_user_cannot_activate_eamil_with_invalid_token(self):
        
        token = jwt.encode({"user_id": 31264658}, "klfdjlkfdl", algorithm="HS256")
        res = self.client.get(f"/api/users/verify-email/?token={token}")   
        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.data["Token"], 'Token is invalid or expired')


    def test_user_cannot_activate_already_activated_email(self):
        user = User.objects.create_user(
            name="Jhon Adam",
            email= self.user_data['email'], 
            username= self.user_data['username'],
            password=self.user_data['password']
        )
        user.is_verified = True
        user.save()
        token = RefreshToken.for_user(user).access_token
        res = self.client.get(f"/api/users/verify-email/?token={token}")   
        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.data["email"], 'Your Email is Already Activated')


    def test_resend_user_new_activation_email(self):
        user = User.objects.create_user(
            name="Jhon Adam",
            email= self.user_data['email'], 
            username= self.user_data['username'],
            password=self.user_data['password']
        )
        data = {
            "email":user.email
        }
        res = self.client.post("/api/users/resend-verify-email/", data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data["email"], "Email sent")

    def test_cannot_resend_user_new_activation_email_for_nonexisting_email(self):
        data = {
            "email":"email@eamil.com"
        }
        res = self.client.post("/api/users/resend-verify-email/", data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(res.data["email"], "Email does not exist.")

    def test_cannot_resend_user_new_activation_email_to_activated_email(self):

        user = User.objects.create_user(
            name="Jhon Adam",
            email= self.user_data['email'], 
            username= self.user_data['username'],
            password=self.user_data['password']
        )
        user.is_verified = True
        user.save()

        data = {
            "email": user.email
        }
        res = self.client.post("/api/users/resend-verify-email/", data)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.data["email"], "Your email address already activated.")

    def test_user_can_login(self):
        user = User.objects.create_user(
            name="Jhon Adam",
            email= self.user_data['email'], 
            username= self.user_data['username'],
            password=self.user_data['password']
        )
        user.is_verified = True
        user.save()
        data = {
            "username": user.username,
            "password": self.user_data['password']
        }
        res = self.client.post("/api/users/login/", data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data['username'], user.username)
        self.assertIsNotNone(res.data['tokens'])

    def test_user_cannot_login_if_not_verified_email(self):
        user = User.objects.create_user(
            name="Jhon Adam",
            email= self.user_data['email'], 
            username= self.user_data['username'],
            password=self.user_data['password']
        )
        data = {
            "username": user.username,
            "password": self.user_data['password']
        }
        res = self.client.post("/api/users/login/", data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(res.data["detail"], "Your email address is not verified")
        
    def test_user_cannot_login_with_wrong_credentials(self):
        data = {
            "username": "someuser",
            "password": "somepassword"
        }
        
        res = self.client.post("/api/users/login/",data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(res.data['detail'], "Invalid credintials, Please try again")

    def test_user_cannot_login_without_password(self):
        data = {
            "username": "someuser",
            "password": ""
        }
        res = self.client.post("/api/users/login/",data)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.data['password'], ["This field may not be blank."])

    def test_user_cannot_login_without_username(self):
        data = {
            "username": "",
            "password": "someuser"
        }
        res = self.client.post("/api/users/login/",data)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.data['username'], ["This field may not be blank."])

class TestUserProfileAPIView(TestSetUp):
    def test_profile_is_created_automaticaly_on_register_and_list_retrive_profile(self):
        user_1 = self.client.post("/api/users/register/", self.user_data)
        self.assertEqual(user_1.status_code, 201)
        profile = Profile.objects.all().count()
        self.assertEqual(profile, 1)
        
        list_res = self.client.get("/api/users/profile/")
        self.assertEqual(list_res.status_code, 200)

        retrive_res = self.client.get("/api/users/profile/1/")
        self.assertEqual(retrive_res.status_code, 200)
        self.assertEqual(retrive_res.data['user'], user_1.data['username'])


    def test_user_can_update_or_partially_update_his_profile_and_not_if_unauthorized(self):
        user_1 = self.client.post("/api/users/register/", self.user_data)
        user = User.objects.get(username=user_1.data["username"])
        token = RefreshToken.for_user(user).access_token

        data = {
            "phone":"01122334455"
        }
        res = self.client.patch("/api/users/profile/2/", data, HTTP_AUTHORIZATION=f'Bearer {token}')
        self.assertEqual(res.status_code, 200)

        unauth_res = self.client.patch("/api/users/profile/2/", data)
        self.assertEqual(unauth_res.status_code, 401)


        data = {
            "phone": "01155221199",
            "age": 27,
            "weight": 90,
            "height": 175,
            "image": SimpleUploadedFile(
                        name='test_image.jpg',
                        content=open("media/users/images/default-avatar.png", 'rb').read(), 
                        content_type='image/jpeg'),
            "gender": 'male'
        }
        res = self.client.put("/api/users/profile/2/", data, HTTP_AUTHORIZATION=f'Bearer {token}')
        self.assertEqual(res.status_code, 200)
        
        unauth_res = self.client.put("/api/users/profile/2/", data)
        self.assertEqual(unauth_res.status_code, 401)