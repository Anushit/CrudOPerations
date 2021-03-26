from rest_framework.response import Response
from rest_framework import status
from .serializers import AuthUserSerializer
from rest_framework.decorators import api_view
from .forms import *
from datetime import datetime
from django.core.paginator import Paginator


@api_view(['POST'], )
def UserCreateAPIView(request):
    form = UserRegisterForm(data=request.POST)
    print(form)
    if form.is_valid():
        serializer = AuthUserSerializer(data=form.cleaned_data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'successfully signup'}, status=status.HTTP_201_CREATED)
        else:
            data = {"data": serializer._errors}
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

    data = {'data': form._errors}
    return Response(data, status=status.HTTP_400_BAD_REQUEST)