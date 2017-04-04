from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound

def index(request):
	return render(request, 'coffeeshop/index.html')# Create your views here.
