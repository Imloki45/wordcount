from django.http import HttpResponse
from django.shortcuts import render
def home(request):
  return render(request,'home.html')
def count(request):
  dis=request.GET['text']
  l=len(dis.split())
  return render(request,'co.html',{"text":dis,"len":l})
def about(request):
  return render(request,'about.html')