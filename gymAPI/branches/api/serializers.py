from os import access
from rest_frmework import serializers
from branches.models import Branch
from rest_framework.exceptions import ParseError
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken, TokenError

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        # fields = '_all_'
        fields = ["name", "address", "description", "phone"]
