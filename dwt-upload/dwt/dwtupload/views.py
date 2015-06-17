from django.shortcuts import render
from django.http import HttpResponse
import os

# Create your views here.
def home(request):
    return render(request, 'index.htm', {'what':'DWT File Upload with Django'})

def upload(request):
    if request.method == 'POST':
        handle_uploaded_file(request.FILES['RemoteFile'], str(request.FILES['RemoteFile']))
        return HttpResponse("Successful")

    return HttpResponse("Failed")

def handle_uploaded_file(file, filename):
    if not os.path.exists('upload/'):
        os.mkdir('upload/')

    with open('upload/' + filename, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
