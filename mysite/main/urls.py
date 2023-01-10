from django.urls import path  #untuk mengambil url path
from . import views #import file views.py di folder main

#note : 
#file view.py sama seperti file CONTROLLERS.PHP di CI

urlpatterns = [
    path("",views.index, name = "index"),
    path("kelas",views.kelas,name = "kelas"),
    path("siswa",views.siswa,name="siswa"),
    path("siswa_add",views.siswa_add,name = "add_siswa"),
    path("siswa_read",views.siswa_read,name = "read_siswa"),
    path("siswa_read_detail",views.siswa_read_detail,name = "read siswa_detail"),
    path("siswa_edit/<id>",views.siswa_edit,name="edit_siswa"),
    path("siswa_delete/<id>",views.siswa_delete,name = "delete_siswa"),
    path("login",views.login,name = "login")
    
]
