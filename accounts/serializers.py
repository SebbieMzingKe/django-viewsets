from rest_framework import serializers
from .models import User
from rest_framework.validators import ValidationError

class SignUPSerializer(serializers.ModelSerializer):
        #validations

        email = serializers.CharField(max_length = 80)
        username = serializers.CharField(max_length = 45)
        password = serializers.CharField(min_length = 8, write_only = True)

        class Meta:
                model = User
                fields = ["email", "username", "password"]

                #checking whether the user exists in our db

                def validate(self, attrs):
                    email_exists = User.objects.filter(email = attrs["email"]).exists()
                    if email_exists:
                        raise validationError("email has already been used")
                    return super().validate(attrs)
