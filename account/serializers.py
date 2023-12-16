from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.Number = validated_data['Number']
        instance.Portfolio_amount = validated_data['Portfolio_amount']
        instance.Image = validated_data['Image']
        instance.Desc = validated_data['Desc']
        instance.occupation = validated_data['occupation']

        instance.save()

        return instance