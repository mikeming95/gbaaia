from django.shortcuts import *
from django.views.generic import View
from django.shortcuts import render,render_to_response
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views import generic
# Create your views here.

class Index(View):
    def get(self, request):
        return render_to_response("login.html")

def mainpage(request):
    if request.method == 'POST':
        password=request.POST.get('password')
        with open("./password.txt","r") as f:
            lines=f.readlines()
            txtpassword=lines[0]
        if(password== txtpassword):
            return render_to_response("index.html")
        else:
            return render_to_response("login.html")
        #return render(request, 'result.html', {'content': content})
    else:
        return render_to_response("login.html")
