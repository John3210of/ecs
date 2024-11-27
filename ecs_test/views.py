from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.db import connection
import socket

@api_view(['GET'])
def index(request):
    '''
        model에 대해 정의 하지 않고, 조회만 시도합니다.
        load balancer 정상 작동 검증을 위해 현재 서버의 ip를 같이 출력합니다.
    '''
    server_ip = socket.gethostbyname(socket.gethostname())
    with connection.cursor() as cursor:
        cursor.execute("SELECT id, name, age, gender, region FROM user")
        columns = [col[0] for col in cursor.description]
        users = [dict(zip(columns, row)) for row in cursor.fetchall()]

    data = {
        "result": "success",
        "data": users,
        "server_ip": server_ip
    }
    return Response(data, status=status.HTTP_200_OK)
