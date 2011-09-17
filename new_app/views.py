# Create your views here.
import os
from new_app import models
from django.shortcuts import render_to_response
from django.template import Context

def home(request):
    app_name = os.path.basename(os.path.dirname(__file__))
    data = models.Something.objects.all()
    return render_to_response('home.html', Context(locals()))
    
