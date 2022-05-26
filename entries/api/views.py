from tkinter import Entry
from rest_framework.response import Response
from entries.api.serializers import  EntrySerializer
from rest_framework.views import APIView
from entries.models import Entry


class EntryListAPi(APIView):
    def get(self,request):
        entries= Entry.objects.all()
        serializer = EntrySerializer (entries, many =True)
        
        return Response(serializer.data)
    
    # Me llegan unos datos en el request los cojo y los apunto en la database 
    def post (self, request):
        serializer = EntrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=201)

        return Response(status=400, data=serializer.errors)
    
    def put(self, request):
         
         
        
        pass
    
    def delete(request, id):
        entries = Entry.objects.all()
        entries.delete()
        
        return Response(('Todo OK'))
        
