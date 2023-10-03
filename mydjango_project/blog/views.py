from django.shortcuts import render
from django.http import HttpResponse
import json, logging, os,os.path

# Create your views here.
# load template || render || to HttpResponse 

contextJson = None
dataPath = os.path.dirname(__file__) + '/data.json'
with open(dataPath,'r') as fr:
    contextJson = json.loads(fr.read())
    #logging.logger

def home(request):
    return render(request,'blog/home.html', contextJson)