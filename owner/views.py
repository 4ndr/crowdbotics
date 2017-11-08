from rest_framework import viewsets
from .serializers import CatSerializer, DogSerializer
from pet.models import Dog, Cat

class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer

class DogViewSet(viewsets.ModelViewSet):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer