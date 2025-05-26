from json import JSONDecodeError
from django.http import JsonResponse
from .serializers import ContactSerializer
from rest_framework.parsers import JSONParser
from rest_framework import views, status
from rest_framework.response import Response



class ContactAPIView(views.APIView):
    """
    A simple APIView for creating contact entires.
    """
    #kontaktira sirilajzer sa metodama dole
    serializer_class = ContactSerializer
    #metoda uzimanja serializer-a in API view
    def get_serializer_context(self):
        return {
            'request': self.request,
            'format': self.format_kwarg,
            'view': self
        }
    #metoda uzimanja serializer-a in API view
    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)

    #najbitnije!
    #ocekujemo da ce JSON biti poslat od klijenta
    #pasujemo taj JSON koristeci passer koje je ugradjen u DJANGO framework
    #saljemo te podatke serializeru da serializuje info (point it to the right fields)
    #ako je info koji dolazi validan (name, massage, email-i ako je email data tip)
    #sacuvam serializer i on sacuva to u DB 
    #saljes nazad info frontend-u
    def post(self, request):
        try:
            data = JSONParser().parse(request)
            serializer = ContactSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except JSONDecodeError:
            return JsonResponse({"result": "error","message": "Json decoding error"}, status= 400)
