from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import StudentSerializer
from rest_framework.permissions import IsAuthenticated
from .send import send

# Create your views here.

def home(request):
    context={}
    return render(request,"home.html",context)

class TestView(APIView):
    # permission_classes = (IsAuthenticated,)
    def get(self,request,*args,**kwargs):
            context = {}
            return Response(context)


    def post(self,request,*args,**kwargs):
        parmission_classes = (IsAuthenticated,)
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            # serializer.save()
            data = dict(serializer.data)
            data_list = [*data.values()]
            send(f"from : {data_list[0]} || name : {data_list[1]} || subject : {data_list[2]} || number_phone : {data_list[3]} || context : {data_list[4]}")
            return Response({"the operation":"successfully done"})
        return Response(serializer.errors)