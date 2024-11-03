from .models import User
from  rest_framework import generics, viewsets, mixins
from .serializers import RegisterSerializer, UserSerializer
class RegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    serializer_class.save

class UserViewSet(mixins.ListModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Create your views here.
