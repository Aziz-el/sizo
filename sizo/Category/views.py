from .models import Category
from  rest_framework import generics, viewsets, mixins
from .serializers import CategorySerializer

class CreateCategory(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    serializer_class.save


class CategoryViewSet(mixins.ListModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
