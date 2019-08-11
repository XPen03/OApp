from django.shortcuts import render
from rest_framework import viewsets
from .models import Picture
from .serializers import PictureSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import PictureSerializer

from . import alternative
# Create your views here.

class PictureView(viewsets.ModelViewSet):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer

    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):

        image_serializer = PictureSerializer(data=request.data)
        #image_serializer.update(self,,alternative.prt("name"))
        Picture.objects.filter(id=11).update(name=alternative.prt("name"))

        if image_serializer.is_valid():
            image_serializer.save()
            return Response(image_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(image_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
