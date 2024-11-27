from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import socket

@api_view(['GET'])
def index(request):
    server_ip = socket.gethostbyname(socket.gethostname())
    data = {"result": "success",
            "data": [{"id":"john", "name":"한"},
                     {"id":"hi", "name":"world"}],
            "server_ip": server_ip
            }
    return Response(data, status=status.HTTP_200_OK)
