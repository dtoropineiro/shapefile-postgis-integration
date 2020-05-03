from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from uploads.core.models import Shapefile
from uploads.core.forms import ShapefileForm
import subprocess
from subprocess import Popen, PIPE, STDOUT

def home(request):
    shapefiles = Shapefile.objects.all()
    return render(request, 'core/home.html', { 'shapefiles': shapefiles })


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'core/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'core/simple_upload.html')


def model_form_upload(request):
    if request.method == 'POST':
        form = ShapefileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ShapefileForm()
    return render(request, 'core/model_form_upload.html', {
        'form': form
    })

def list_shapefiles(request):
    data = Shapefile.objects.all()
    context = {'list': data} 
    return render(request, 'core/shapefile_list.html', context)

def run_script(request):
    print('Hello, friend')
    p1=Popen(['shp2pgsql','-s'])
    data = Shapefile.objects.all()
    context = {'list': data} 
    return render(request, 'core/converted.html', context)
