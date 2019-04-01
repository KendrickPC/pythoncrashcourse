from django.shortcuts import render

def index(request):
	""" The home page for BlogPost"""
	return render(request, 'BlogPost/index.html')
	
