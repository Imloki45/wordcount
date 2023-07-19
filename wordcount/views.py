import json,os
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
  return render(request,'home.html')
def count(request):
  if request.method == "POST":
    dis=request.POST["text"]
  l=len(dis.split())
  charscount=len(dis)
  return render(request,'co.html',{"text":dis,"len":l,"charCount":charscount})
def about(request):
  return render(request,'about.html')
def displayBooks(request):
  # print(os.getcwd())
  # print(open('wordcount\\books.json')) 
  return render(request,'displayBooks.html',{"books":json.load(open('wordcount\\books.json'))})

