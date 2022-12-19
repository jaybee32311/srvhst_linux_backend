from gc import callbacks
from urllib import request
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ImagesSerializer
from back.models import Images, user_directory_path
from rest_framework.generics import ListAPIView

from rest_framework.parsers import MultiPartParser, FormParser

from cryptography.fernet import Fernet

class ImageViewSet(ListAPIView):
    parser_classes = [MultiPartParser, FormParser]
    serializer_class = ImagesSerializer
    def post(self, request, *args, **kwargs):
        
        fernet = Fernet("9xokJqBPVmVntxXWr8euR205P-5GtK40H1HHbsg9F_w=")
        file = request.data['image']
        img = Images()
        img.image = file
        img.mac = fernet.decrypt(str(request.GET.get('mac'))).decode("ASCII")
        img.save()
        callback = Response(status=200)
        
        return callback
@api_view(['POST'])
def delete_image(request):
    image = Images.objects.get(id=request.POST.get('img_id'))
    image.delete()
    callback = Response(status=200)
    return callback
@api_view(['GET'])
def api_test(request):
    return Response('Hello api!')
