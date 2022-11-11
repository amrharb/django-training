from rest_framework import serializers
from users.models import User
from rest_framework.validators import UniqueValidator


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email','username','password1','password2']

    username = serializers.CharField(write_only=True)
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    def validate(self, data):
        if data.get('password1') != data.get('password2'):
            raise serializers.ValidationError("please rewrite the password correctly")
        if len(data.get('password1')) < 8:
            raise serializers.ValidationError("password should be 8 characters or more")
        return data

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password1'])
        user.set_password(validated_data['password2'])
        user.save()
        return user