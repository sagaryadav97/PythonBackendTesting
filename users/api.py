from users.models import  Users
from rest_framework import viewsets, permissions
from .serializer import Userserialer

#create api 

class Userviewset(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = Userserialer