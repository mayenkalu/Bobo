# Import the viewsets class from Django REST Framework's views module. 
# Viewsets are a type of class-based View that provide CRUD operations.
from rest_framework import viewsets

# Import the Baby model from the current module's models.py file.
from .models import Baby

# Import the BabySerializer class from the current module's serializers.py file.
# This class defines how instances of the Baby model are converted to JSON.
from .serializers import BabySerializer

# Define a new viewset for the Baby model.
class BabyViewSet(viewsets.ModelViewSet):
    # The queryset attribute defines the list of objects that this viewset will operate on.
    # In this case, it includes all instances of the Baby model.
    queryset = Baby.objects.all()

    # The serializer_class attribute specifies the serializer class that this viewset will use to
    # convert instances of the Baby model to JSON (when sending responses) and from JSON back to 
    # model instances (when processing incoming requests).
    serializer_class = BabySerializer
