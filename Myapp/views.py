from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from Myapp.models import Mmodel
from .serializers import Empserializer
from rest_framework import status
@api_view(['GET'])
def Home(request):
    return Response('API calling')
@api_view(['GET'])
def Emplist(request):
    data=Mmodel.objects.all()
    serialize=Empserializer(data,many=True)
    return Response(serialize.data)
# Create your views here.

@api_view(['POST'])
def Add_items(request):
    item = Empserializer(data=request.data)
 
    # validating for already existing data 
    if item.is_valid():
        item.save()
        return Response(item.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(['PUT'])
def Update_items(request, pk):
    try:
        item = Mmodel.objects.get(pk=pk)
    except Mmodel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = Empserializer(instance=item, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_items(request, pk):
    item = get_object_or_404(Mmodel, pk=pk)
    item.delete()
    return Response(status=status.HTTP_202_ACCEPTED)