from .models import artist
from .serializers import ArtistSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser,FormParser

class CrudSerializerView(APIView):
    parser_classes = (MultiPartParser,FormParser)

    def get(self,request):
        artobj = artist.objects.all()
        artserializerobj = ArtistSerializer(artobj,many=True)
        return Response(artserializerobj.data)

    def post(self, request, *args, **kwargs):
        serializeobj = ArtistSerializer(data=request.data)
        if serializeobj.is_valid():
            serializeobj.save()
            return Response(serializeobj.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializeobj.errors, status=status.HTTP_400_BAD_REQUEST)






