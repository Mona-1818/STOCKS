from django.shortcuts import render
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view, permission_classes
from .serializers import UserSerializer
from .models import CustomUser
from rest_framework.permissions import IsAuthenticated
from .models import UserProfile, portfolio
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
def user_login(request):
    if request.method == 'POST':
        request_data = json.loads(request.body)
        username = request_data.get('username')
        email = request_data.get('email')
        password = request_data.get('password')
        print(username)

        user = None
        if '@' in username:
            try:
                user = CustomUser.objects.get(email=username)
            except ObjectDoesNotExist:
                pass

        if not user:
            user = authenticate(username=username, password=password)

        if user:
            token, _ = Token.objects.get_or_create(user=user)
            print()
            return Response({'email':email,'username':username, 'token': token.key}, status=status.HTTP_200_OK)

        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user_logout(request):
    if request.method == 'POST':
        try:
            request.user.auth_token.delete()
            return Response({'message': 'Successfully logged out.'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
     
@csrf_exempt
@api_view(['POST']) 
def update_user(request, username):
    try:
        profile = UserProfile.objects.get(username=username)
    except UserProfile.DoesNotExist:
        return Response({'message': 'User profile not found.'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'POST':
        profile.email = request.data.get('email', profile.email)
        profile.username = request.data.get('username', profile.username)
        profile.name = request.data.get('name', profile.name)
        profile.Number = request.data.get('phone_number', profile.Number)
        profile.Portfolio_amount = request.data.get('Portfolio_amount', profile.Portfolio_amount)
        profile.Desc = request.data.get('Desc', profile.Desc)
        profile.occupation = request.data.get('occupation', profile.occupation)

  
        profile.save()
        
        return Response({'message': 'profile updated.'}, status=status.HTTP_200_OK)
    else:
        return Response({'message': 'internal error.'}, status=status.HTTP_400_BAD_REQUEST)

    
    
   
@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def create_user(request, username):
    user = CustomUser.objects.get(username=username)
    if request.method == 'POST':
        data = UserProfile(
            email = user.email,
            username = user,
            name=request.data.get('name'),
            Number=request.data.get('Number'),
            Portfolio_amount=request.data.get('Portfolio_amount'),
            Desc=request.data.get('Desc'),
            occupation=request.data.get('occupation')
        )
        data.save()
        
        return Response({'message': 'profile created.'}, status=status.HTTP_200_OK)
    else:
        return Response({'message': 'internal error.'}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
def add_Portfolio(request, username):
    if request.method == 'POST':
        try:
            request_data = json.loads(request.body)
            data_array = request_data.get('data', [])
            for i in data_array:
                instance = portfolio(
                    username = username,
                    companyname = i['name'],
                    quantity = i['quantity'],
                    price = i['price']
                )
                instance.save()
            return Response({'message': 'Data received.'}, status=status.HTTP_200_OK)
        except json.JSONDecodeError:
            return Response({'message': 'Invalid JSON format'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'message': 'Invalid request method'}, status=status.HTTP_400_BAD_REQUEST)