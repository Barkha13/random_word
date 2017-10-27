from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string


# Create your views here.
def index(request):
    if 'count' not in request.session:
        request.session['count'] = 0
    if 'unique_id' not in request.session:
        request.session['unique_id']= ""
    return render(request,"random_word_gen/index.html")

def generate(request):
    request.session['count']+=1
    request.session['unique_id'] = get_random_string(length=14)
    return redirect('/')

def reset(request):
    del request.session['count']
    del request.session['unique_id']
    return redirect('/')
    
               
    
