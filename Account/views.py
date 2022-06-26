


from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import OTPSerializer, UserRegisterSerializer, UserSerializer
from rest_framework import status
# from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from Utils.otp import get_random_otp
from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.
User = get_user_model()

OTPCODE = ''


class UserRegisterView(APIView):
    def post(self, request):
        ser_data = UserRegisterSerializer(data=request.POST)
        if ser_data.is_valid():
            # TODO send Activation Code:1234
            global OTPCODE
            OTPCODE = str(get_random_otp())
            print(f'{OTPCODE} is OTPCODE')
            ser_data.create(ser_data.validated_data)
            global USER_MOBILE
            USER_MOBILE = str(request.data['User_mobile'])
            return Response(ser_data.data, status=status.HTTP_201_CREATED)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)
        # return redirect('account.send_otp')


class SendOTP(APIView):
    def post(self, request):
        try:
            otp = request.data['otp']
            queryset = User.objects.filter(User_mobile=USER_MOBILE)
            if bool(queryset.values("is_active")[0]["is_active"]):
                return Response({'USER IS ALREADY ACTIVE'}, status=status.HTTP_400_BAD_REQUEST)
            ser_data = OTPSerializer(data=request.POST)
            if ser_data.is_valid() and str(otp) == OTPCODE:
                # TODO:is_active=True
                queryset.update(is_active=True)
                return Response(ser_data.data, status=status.HTTP_200_OK)
            return Response({'message': 'INVALID OTP'}, status=status.HTTP_400_BAD_REQUEST)
        except ( NameError,):
            return Response({'message': 'MOBILE NUMBER NOT FOUND'}, status=status.HTTP_400_BAD_REQUEST)
        except(MultiValueDictKeyError,):
            return Response({'message': 'Error oucerd'}, status=status.HTTP_400_BAD_REQUEST)


class UserUpdateInfo(APIView):
    def post(self, request):
        
        usr=request.user
        ser_data = UserSerializer(instance=request.POST)
        if ser_data.is_valid():
            ser_data.update(ser_data.validated_data)
            return Response(ser_data.data, status=status.HTTP_201_CREATED)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)
        