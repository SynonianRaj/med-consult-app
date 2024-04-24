from django.shortcuts import render
from django.http import HttpResponse
from .models import Doctor,Specialization
# Create your views here.
def homeview(request):
    return render(request,'home/index.html')
    
def choose_services(request):
    s = Specialization.objects.all()
    return render(request,'home/services.html',{'specialization':s})

def doctor_list(request,id):
    d = Doctor.objects.filter(specialization=id)
    return render(request,'home/doctor-list.html',{'doctors':d})
