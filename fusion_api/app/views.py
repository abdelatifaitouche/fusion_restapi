from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Sneakers
from .serializers import *
from rest_framework.decorators import api_view




@api_view(['GET'])
def getRoutes(request):
    api_routes = [
        '/products',
        '/product_details/<str:pk>',
        '/create_product',
        '/addCommande'
    ]
    return Response(api_routes)


@api_view(['GET'])
def getProducts(request):
    sneakers = Sneakers.objects.all()
    sneakers_serializer = SneakersSerializers(sneakers , many = True)
    return Response(sneakers_serializer.data)

@api_view(['GET'])
def getProductDetails(request , pk):
    sneaker = Sneakers.objects.get(id = pk)
    sneaker_serializer = SneakersSerializers(sneaker , many = False)
    return Response(sneaker_serializer.data)


@api_view(['POST'])
def createProduct(request):
    sneakerSerializer = SneakersSerializers(data = request.data)
    if sneakerSerializer.is_valid():
        sneakerSerializer.save()
    else : 
        print('can t create')
    return Response(sneakerSerializer.data)



@api_view(['POST'])
def addCommande(request):
    commandeSerailizer = CommandeSerializers(data = request.data)
    if commandeSerailizer.is_valid():   
        commandeSerailizer.save()
    else : 
        print('can t crate' )
    return Response(commandeSerailizer.data)






"""
class SneakersListApiView(APIView):
    # add permission to check if user is authenticated

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        todos = Sneakers.objects.all()
        serializer = SneakersSerializers(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SneakersDetailApiView(APIView):
    # add permission to check if user is authenticated
    

    def get_object(self, todo_id):
        '''
        Helper method to get the object with given todo_id, and user_id
        '''
        try:
            return Sneakers.objects.get(id=todo_id)
        except Sneakers.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, todo_id, *args, **kwargs):
        '''
        Retrieves the Todo with given todo_id
        '''
        todo_instance = self.get_object(todo_id)
        if not todo_instance:
            return Response(
                {"res": "Object with todo id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = SneakersSerializers(todo_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)






"""