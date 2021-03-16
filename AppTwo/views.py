from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User
# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello Ahh!!!</h>")

def help(resquest):
    my_dict = {
    'insert_me':'You want any help'
    }
    return render(resquest,'index.html',context = my_dict)

def show(resquest):
    data = User.objects.order_by('first_name')

    my_dict = {
        'all_data':data,
    }
    return render(resquest,'index.html',context = my_dict)
