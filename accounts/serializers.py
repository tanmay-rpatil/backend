from asyncore import write
from dataclasses import fields
from wsgiref.validate import validator
from .models import Application, CustomUser

from django.contrib.auth.password_validation import validate_password

from rest_framework import serializers,status
from rest_framework.response import Response
from rest_framework.validators import UniqueValidator

class CustomUserSerializer(serializers.ModelSerializer):
	class Meta:
		model = CustomUser
		fields = ['id','username','email','first_name','last_name','properties']

class RegisterSerializer(serializers.ModelSerializer):
	#unqiue email
	email = serializers.EmailField(required=True,
									validators=[UniqueValidator(queryset=CustomUser.objects.all())])
	password = serializers.CharField(write_only=True,
									required=True,
									validators=[validate_password])

	class Meta:
		model = CustomUser
		fields = ('username','password','email','first_name','last_name','properties')
		extra_kwargs = {
			'first_name': {},
			'last_name': {}
		}
	def create(self, validated_data):
		user = CustomUser.objects.create(
			username=validated_data['username'],
			email=validated_data['email'],
			first_name=validated_data['first_name'],
			last_name=validated_data['last_name'],
			properties=validated_data['properties'],
		)
		user.set_password(validated_data['password'])
		user.save()
		return user

	