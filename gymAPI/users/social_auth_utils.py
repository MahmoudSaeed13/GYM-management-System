from rest_framework.exceptions import AuthenticationFailed
from users.models import User
import os
from django.contrib.auth import authenticate
import random
from users.models import Profile

def generate_username(name):

    username = "".join(name.split(' ')).lower()
    if not User.objects.filter(username=username).exists():
        return username
    else:
        random_username = username + str(random.randint(0, 100000))
        return generate_username(random_username)


def register_social_user(provider, user_id, email, name):
    filtered_user_by_email = User.objects.filter(email=email)

    if filtered_user_by_email.exists():
        if provider == filtered_user_by_email[0].auth_provider:
            print(email)
            password = os.environ.get("SOCIAL_SECRET")
            registered_user = User.objects.get(email=email)
            print(registered_user)
            return {
                "username" : registered_user.username, 
                "email" : registered_user.email,
                "tokens" : registered_user.tokens()
            }
        else:
            raise AuthenticationFailed(
                detail='Please continue your login using ' +
                filtered_user_by_email[0].auth_provider
                )

    else:
        user = {
            "name": name,
            "username" : generate_username(name),
            "email"  :email,
            "password" : os.environ.get("SOCIAL_SECRET")
        }

        user = User.objects.create_user(**user)
        user.is_verified = True
        user.auth_provider = provider
        user.save()

        Profile.objects.create(user=user)

        return {
            'username': user.username,
            'email': user.email,
            'tokens': user.tokens()
        }