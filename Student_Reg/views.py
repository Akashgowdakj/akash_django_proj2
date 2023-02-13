from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(Request):
    return render(Request,'Student_Reg/home.html')
    # return HttpResponse("This is my home page")

def reg(Request):
    return render(Request,'Student_Reg/reg.html')
    # return HttpResponse("This is my Registration page")

def report(Request):
    return HttpResponse("This is my Report page")

