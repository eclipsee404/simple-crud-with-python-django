from django.db import models

# Create your models here.

class Kelas(models.Model):
    nama_kelas = models.IntegerField()
    
    class Meta:
        db_table = "kelas"

class Siswa(models.Model):
    nama_depan = models.CharField(max_length=255)
    nama_belakang = models.CharField(max_length=255)
    kelas_id = models.IntegerField(default=0)
    
    class Meta:
        db_table = "siswa"