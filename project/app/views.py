from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .serializers import *
from .models import *
# Create your views here.
def fun(request):
    return JsonResponse({'name':'Vysakh','age':12})

def fun2(request):
    if request.method=='GET':
        d=student.objects.all()
        s=sample(d,many=True)
        return JsonResponse(s.data,safe=False)