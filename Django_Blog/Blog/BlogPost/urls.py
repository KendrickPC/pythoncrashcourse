""" Defines URL patterns for BlogPost"""

from django.urls import path

from . import views

app_name='BlogPost'
urlpatterns = [
	# Home page.
	path('', views.index, name='index'),
]


