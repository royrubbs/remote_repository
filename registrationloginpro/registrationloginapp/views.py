from django.shortcuts import render
from .models import RegistrationData
from .forms import RegistrationForm,LoginForm
from  django.http.response import JsonResponse
import json
def home(request):
    return render(request,'reglogin.html')

def registration(request):
    try:
        if request.method=='POST':
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            data=RegistrationData(**body)
            data.save()
            resp={
                'status':'success',
                'code':200,
                'message':'registered successfully.'
            }
            return JsonResponse(resp)
    except Exception:
        resp={
            'code':409,
            'status':'failed',
            'message':"Invalid Input."
        }
        return JsonResponse(resp,status=409)

def login(request):
    if request.method=="POST":

            email=request.POST.get('email','')
            password1=request.POST.get('password1','')
            user=RegistrationData.objects.filter(email=email,password1=password1)
            if user:
                resp={
                    'status':'Success',
                    'code':200,
                    'message':"Login Successfull."
            }
            return JsonResponse(resp)
        else:
                resp = {
                    'status': 'failed',
                    'code':401,
                    'message': "Unauthorized Login."

                }
                return JsonResponse(resp)
