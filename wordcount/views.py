from django.http import HttpResponse
from django.shortcuts import render
def home(request):
  return render(request,'home.html')
def count(request):
  if request.method == "POST":
    dis=request.POST["text"]
  l=len(dis.split())
  return render(request,'co.html',{"text":dis,"len":l})
def about(request):
  return render(request,'about.html')
    
