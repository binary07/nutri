from .models import (
    Specialty,
    Nutritionist,
)
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class SpecialtySerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialty
        fields = [
            'id',
            'name',
        ]


class NutritionistSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(
        source='user.id',
        read_only=True,
    )
    email = serializers.EmailField(
        source='user.email',
        required=False,
    )
    first_name = serializers.CharField(
        source='user.first_name',
        required=False,
    )
    last_name = serializers.CharField(
        source='user.last_name',
        required=False,
    )
    second_lastname = serializers.CharField(
        source='user.second_lastname',
        required=False,
    )
    phone = serializers.CharField(
        source='user.phone',
        required=False,
    )
    password = serializers.CharField(
        source='user.password',
        style={'input_type': 'password'},
        required=False,
    )
    specialties = serializers.PrimaryKeyRelatedField(
        queryset=Specialty.objects.all(), 
        many=True,
    )

    class Meta:
        model = Nutritionist
        fields = [
            'id',
            'email',
            'first_name',
            'last_name',
            'second_lastname',
            'phone',
            'license',
            'degree',
            'specialties',
            'password',
        ]

    def create(self, validated_data):
        user = User(
            username = validated_data['user']['phone'],
            first_name = validated_data['user']['first_name'],
            last_name = validated_data['user']['last_name'],
            second_lastname = validated_data['user']['second_lastname'],
            email = validated_data['user']['email'],
            phone = validated_data['user']['phone'],
            is_patient=False,
            is_nutritionist=True,
        )
        user.set_password(validated_data['user']['password'])
        user.save()
        nutritionist = Nutritionist.objects.create(
            user=user,
            license = validated_data['license'],
            degree = validated_data['degree'],
        )
        nutritionist.specialties.add(*validated_data['specialties'])
        nutritionist.save()
        return nutritionist

    def update(self, instance, validated_data):
        if 'user' in validated_data:
            if 'first_name' in validated_data['user']:
                instance.user.first_name = validated_data['user']['first_name']
            if 'last_name' in validated_data['user']:
                instance.user.last_name = validated_data['user']['last_name']
            if 'second_lastname' in validated_data['user']:
                instance.user.second_lastname = validated_data['user']['second_lastname']
            if 'email' in validated_data['user']:
                instance.user.email = validated_data['user']['email']
            if 'phone' in validated_data['user']:
                instance.user.phone = validated_data['user']['phone']
            instance.user.save()

        return instance
