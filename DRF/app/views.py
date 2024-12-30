from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from .serializers import *
from .models import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
# Create your views here.
# def fun1(request):
#     return JsonResponse({'name':'Vysakh'})

# def fun1(request):
#     if request.method=='GET':
#         data=student.objects.all()  
#         s=studSerializer(data,many=True)
#         return JsonResponse(s.data,safe=False)
@csrf_exempt
def fun1(request):
    if request.method=='GET':
        data=student.objects.all()  
        s=studModelSerializer(data,many=True)
        return JsonResponse(s.data,safe=False)
    elif request.method=='POST':
        d=JSONParser().parse(request)
        s=studModelSerializer(data=d)
        print(s)
        if s.is_valid():
            s.save()
            return JsonResponse(s.data,safe=False)
        else:
            return JsonResponse(s.errors)