from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from main.models import Siswa,Kelas
from django.core import serializers
from django.db import connection
import json
# Create your views here.


def index(response):
    # return HttpResponse("<h1>Tech with tim!</h1>")
    return render(response,"main/home.html")

def home(response):
    return render(response,"main/home.html")

def kelas(response):
    return render(response,"main/kelas.html")

def siswa(response):
    kelas = Kelas.objects.all()
    datanya= {
        'kelas':kelas,
        'page':"ini page"
    }
    return render(response,"main/siswa.html",datanya)

def siswa_add(request):
    siswa = Siswa(
        nama_depan=request.POST['nama_depan'],
        nama_belakang=request.POST['nama_belakang'],
        kelas_id=request.POST['kelas_id'],
    )
    siswa.save()
    return redirect('/')

def siswa_read(request):
    siswa = Siswa.objects.raw("select a.nama_depan,a.nama_belakang,a.id,b.nama_kelas from siswa as a left join kelas as b on a.kelas_id = b.id")
    kelas = Kelas.objects.all()
    datanya= {
        'siswa': siswa,
        'kelas':kelas,
        'page':"ini page"
    }
    return render(request,'main/tampil_siswa.html',datanya)

def siswa_read_detail(request):
    siswa = Siswa.objects.filter(id=request.POST['id'])
    data = serializers.serialize('json',siswa)
    return HttpResponse(data, content_type='application/json')

def siswa_edit(request,id):
    siswa = Siswa.objects.get(id=id)
    siswa.nama_depan = request.POST['nama_depan']
    siswa.nama_belakang = request.POST['nama_belakang']
    siswa.kelas_id = request.POST['kelas_id']
    siswa.save()
    return redirect('/')

def siswa_delete(request,id):
    siswa = Siswa.objects.get(id=id)
    siswa.delete()
    return redirect('/')

def login(response):
    return render(response,'main/login.html')