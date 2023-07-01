from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view(['POST','GET'])
def get_reply(request):
    return Response({'status':'Working'})