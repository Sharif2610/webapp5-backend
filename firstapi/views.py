from django.shortcuts import render
from . models import Books
from . serializers import BookSerializer,UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes,\
authentication_classes
from rest_framework.status import HTTP_200_OK,\
HTTP_400_BAD_REQUEST,HTTP_201_CREATED
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.authentication import TokenAuthentication
# Create your views here.
@api_view(['GET','POST'])
#@authentication_classes([TokenAuthentication])
#@permission_classes([IsAuthenticated])
def show_api(request):
    if request.method  == 'GET':
        books = Books.objects.all()
        serializer = BookSerializer(books,many=True)
        return Response(serializer.data)
    elif request.method  == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=HTTP_201_CREATED)
        return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)
@api_view(['GET','POST'])
def register_book(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        uobj = serializer.save()
        uobj.set_password(serializer.validated_data['password'])
        uobj.save()
        Token.objects.create(user=uobj)
        return Response(status=HTTP_201_CREATED)
    return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)
