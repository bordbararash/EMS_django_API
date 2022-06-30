

from dataclasses import field, fields
from rest_framework import serializers

from django.contrib.auth import get_user_model

from .models import ActivationCode,City,Unit

User = get_user_model()


def clean_email(value):
    if 'admin' in value:
        raise serializers.ValidationError('admin cant be in email')


class UserRegisterSerializer(serializers.ModelSerializer):
    # password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        # fields = '__all__'
        fields = ('User_national_code', 'User_mobile', 'is_active','password',
                  'IsOrganizationalAccount', 'City', 'Unit')
        extra_kwargs = {
            # 'password': {'write_only': True},
            'User_mobile': {'validators': (clean_email,)}
        }

    def create(self, validated_data):
        validated_data['is_active'] = False
        return User.objects.create_user(**validated_data)

    def validate_User_national_code(self, value):
        if value == '123':
            raise serializers.ValidationError('User_national_code_ErrorFormat')
        return value

    def validate(self, data):
        if  data['IsOrganizationalAccount'] and data['User_national_code']:
            raise serializers.ValidationError('organizational Account does not have national_ID')
        return data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

        def update(self, instance, validated_data):
            instance.s_superuser = validated_data.get(
                's_superuser', instance.s_superuser)
            instance.first_name = validated_data.get(
                'first_name', instance.first_name)
            instance.last_name = validated_data.get(
                'last_name', instance.last_name)
            instance.email = validated_data.get('email', instance.email)
            instance.is_staff = validated_data.get(
                'is_staff', instance.is_staff)
            instance.is_active = validated_data.get(
                'is_active', instance.is_active)

            instance.save()
            return instance


class OTPSerializer(serializers.Serializer):
    otp = serializers.CharField()

class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model=Unit
        fields=('id','Unit_name','City')
class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model=City
        fields=('id','City_name')
        
