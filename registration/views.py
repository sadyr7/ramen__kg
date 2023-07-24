from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
# lxdlwbubuykzarrx
from registration.send_email import send_confirmation_email
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import permissions
from registration.serializer import RegistrationSerializer,ActivationSerializer,UserSerializer, RegisterPhoneSerializer
User = get_user_model()
# Create your views here.

class RegistrationView(APIView):

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        send_confirmation_email(user.email, user.activation_code)
        if user:
            print(user, '!!!!')
            try:
                send_confirmation_email(user.email,
                                       user.activation_code)
            except:
                return Response({'message':'Зарегистрировался но на почту код не отправился',
                                'data': serializer.data},status=201)
        return Response(serializer.data, status=201)

class ActivationView(GenericAPIView):
    serializer_class = ActivationSerializer

    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response('Успешно активирован', status=200)


class LoginView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)

class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAdminUser,)


class RegistrationPhoneView(APIView):
    def post(self, request):
        data = request.data
        serializer = RegisterPhoneSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response('good', status=201)

