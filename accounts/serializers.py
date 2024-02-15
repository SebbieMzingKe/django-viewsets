from rest_framework import serializers
from .models import User
from rest_framework.validators import ValidationError
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password

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
                    print("validating")
                    email_exists = User.objects.filter(email = attrs["email"]).exists()
                    if email_exists:
                        raise ValidationError("email has already been used")
                    return super().validate(attrs)
                
                
                from django.contrib.auth.hashers import make_password



        def create(self, validated_data):
            password = validated_data.pop('password')
            hashed_password = make_password(password)
            
            user = super().create({**validated_data, 'password': hashed_password})
            user.save()
            Token.objects.create(user = user)
            return user

    