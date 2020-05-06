from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from uploads.core.models import Shapefile
from uploads.core.forms import ShapefileForm
import subprocess
from uploads.core.connection import Connection
import os
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
    con = Connection(os.environ.get('OS'))
    print(con.host)
    context = {'list': data} 
    return render(request, 'core/shapefile_list.html', context)

def run_script(request, id):
    shp = Shapefile.objects.get(id=id)
    user={}
    user["locationepsg"] = "32628"  #EPSG number corresponding to the projection of your shapefile (privided as string)
    host = "postgis-host"
    db_name = "gis"
    schema = "public"
    table = "shp"
    path_to_shape = shp.shapefile.name
    if '.zip' in path_to_shape:
        cmd = 'unzip media/' + path_to_shape +  ' -d ./media/shapefiles/'
        path_to_shape= path_to_shape.replace('.zip','')
        subprocess.call(cmd, shell=True)
    cmd = "shp2pgsql -s 4326 ./media/" +  path_to_shape + " shapefile | psql -h postgis-host -p 5432 -d gis -U docker"
    subprocess.call(cmd, shell=True)
    data = Shapefile.objects.all()
    context = {'list': data} 
    return render(request, 'core/converted.html', context)
