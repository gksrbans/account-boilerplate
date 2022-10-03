from django.http import HttpResponse
from django.shortcuts import render
from .models import User
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def index(request):
    return render(request, 'account/sign.html')

@csrf_exempt
def user_view(request):
    users = User.objects.all()
    users_temp = User()
    name = request.POST['fname']

    try:
        obj = User.objects.get(name=name)
        setattr(obj, name, '3')
        if request.POST['fname'] == 'ez.403':
            level = '3'
        else:
            level = '1'
        obj.save()

    except User.DoesNotExist:
        if request.POST['fname'] == 'ez.4035':
            level = '3'
        else:
            level = '1'
        users_temp.name = name
        users_temp.level = level
        users_temp.save()


    return render(request, 'account/index.html', {"users": users, "levels":level})