from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .forms import MyUserForm
from .models import Images
from django.db.models import Count

from django.http import JsonResponse
from cryptography.fernet import Fernet

from pathlib import Path

# Create your views here.
def index(request):
    '''Index function.'''
    images = Images.objects.values('mac').annotate(dcount=Count('mac')).order_by()
    context = {
        'images': images
    }
    return render(request, 'back/index.html', context)

def pcs_view(request):
    images = Images.objects.filter(mac=request.GET.get("mac")).order_by('created')

    fernet = Fernet("9xokJqBPVmVntxXWr8euR205P-5GtK40H1HHbsg9F_w=")

    for iterating_var in images:
        my_file  = Path(iterating_var.image.url[1:])
        
        if my_file.is_file() == False:
            try:
                Images.objects.get(image=iterating_var.image.url[7:]).delete()
            except:
                continue
    images = Images.objects.filter(mac=request.GET.get("mac")).order_by('created')
    for iterating_var in images:
        with open(iterating_var.image.url[1:], 'rb') as original_file:
                decrypt = fernet.decrypt(original_file.read())
                image_encoded = decrypt.decode('utf-8')
                iterating_var.img_data = "data:image/png;base64,"+image_encoded

    context = {
        'images': images
    }
    return render(request, 'back/pcs.html', context)


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        # check authentication
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('back:index'))
        
        else:
            messages.error(request, 'Wrong username and/or password')
            return HttpResponseRedirect(reverse('back:login'))

    else:
        user_form = MyUserForm()
        context = {
            'form': user_form
        }
        return render(request, 'back/login.html', context)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('back:login'))
