# accounts/serializers.py

# Import User model from the models.py file in the current directory
from .models import User
# Import serializers module from the Django Rest Framework package
from rest_framework import serializers

# UserSerializer is a subclass of ModelSerializer which provides a convenient way 
# to convert complex data types, like Django model instances, into Python datatypes.
class UserSerializer(serializers.ModelSerializer):
    # Nested Meta class contains configuration settings for UserSerializer
    class Meta:
        # Specifies the model to be used, which is User in this case
        model = User
        # Specifies the model fields to be included in the serialization
        fields = ('id', 'username', 'password', 'email')
        # This is an optional setting to apply special behavior to some fields.
        # For example, password can be set to 'write_only' so it won't be readable in serialized format.
        # Currently it's commented out, meaning password field is not write_only.
        # extra_kwargs = {'password': {'write_only': False}}

    # The create method is overridden here to provide custom user creation.
    # 'validated_data' is the cleaned, primitive data that has been validated by the serializer.
    # Here, a new user is created using the validated data and the created user is returned.
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
