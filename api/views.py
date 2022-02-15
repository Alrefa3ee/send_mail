from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import StudentSerializer
from rest_framework.permissions import IsAuthenticated
import smtplib
from email.mime.text import MIMEText
def send(text):
    recipients = ["abd516693@gmail.com"]
    sender = "alrefaeee132@gmail.com"
    subject = "report reminder"
    body = text
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ", ".join(recipients)

    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(sender, 'onifdwhzgfizkwiz')
    send_it = session.sendmail(sender, recipients, msg.as_string())
    session.quit()
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
            
            data = dict(serializer.data)
            data_list = [*data.values()]
            print(type(data_list),type(data))
                         
            msg = f"""from : {data_list[0]} 
            name : {data_list[1]} 
            subject : {data_list[2]} 
            number_phone : {data_list[3]} 
            context : {data_list[4]}"""

            # server.close()
            send(msg)
            return Response({"the operation":"successfully done"})
        return Response(serializer.errors)