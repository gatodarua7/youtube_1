from rest_framework.views import APIView
from rest_framework.response import Response

from .models import UserModel
from .serializer import UserSerializer

class AllUsers(APIView):

    def get(self, request):

        users = UserModel.objects.all()
        user_serializer = UserSerializer(users, many=True)
        return Response(user_serializer.data)
    
    def post(self, request):

        data = {

            'name': request.data['name'],
            'age': request.data['age']

        }


        user_serializer = UserSerializer(data=data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response('Done')
        else:
            return Response('Not done')


class SpecificUser(APIView):

    def get_user(self, id):
        try:
            return UserModel.objects.get(id=id)
        except UserModel.DoesNotExist:
            return Response('Does not exist')
    
    def get(self, request, id):
        user = self.get_user(id)
        user_serializer = UserSerializer(user)
        return Response(user_serializer.data)
    
    def delete(self, request, id):
        user = self.get_user(id)
        user.delete()
        return Response('Deleted with sucessfull')

    def put(self, request, id):
        user = self.get_user(id)
        user_serializer = UserSerializer(user,data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response('Updated with sucessfull, baby')
        else:
            return Response('Try it again, baby')