from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6, required=True)
    password2 = serializers.CharField(min_length=6, required=True, write_only=True)
    first_name = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'password', 'password2']
    
    
    def validate_first_name(self, value):
        if not value.istitle():
            raise serializers.ValidationError('Имя должно начинаться с заглавной буквы!')
        return value

    def validate(self, attrs):
        p1 = attrs.get('password')
        p2 = attrs.get('password2')

        if p1 != p2:
            raise serializers.ValidationError('пароли не совпадают!')
        
        return attrs
    
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            first_name=validated_data['first_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
