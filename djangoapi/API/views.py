from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def getData():
    person = {'name' : 'Abuzar Ali', 'age' : 19, 'stack' : 'Python Full stack Dev'}
    return Response(person) 