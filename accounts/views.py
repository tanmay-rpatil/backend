from .forms import CustomUserCreationForm
from .serializers import CustomUserSerializer,RegisterSerializer

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from knox.models import AuthToken

from rest_framework import generics,permissions
from rest_framework.response import Response

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        user = serializer.save()
        return Response({
            "user": CustomUserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1] })