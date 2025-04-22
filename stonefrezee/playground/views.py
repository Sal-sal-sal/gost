from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest

def say_hello(request):
    return HttpResponse("Hello word")

# Create your views here.
def nigger(request):
    if request.method == 'GET':
       return render(request,'nope.html',{'name':'not'})
    else: return render(request,'hello.html')