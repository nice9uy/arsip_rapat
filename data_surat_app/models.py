from django.db import models

# Create your models here.

class Dbsurat(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    nama = models.CharField(max_length=30)
    surat = models.CharField(max_length=10)
    trak = models.CharField(max_length=30)
    tgl = models.DateField()
    jam = models.CharField(max_length=200)
    tentang = models.CharField(max_length=200)
    upload_file = models.FileField(upload_to='')
 
    def __str__(self):
        return str(self.id)
    
    class Meta:
        db_table = "Dbsurat"


class Kas(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    tgl = models.DateField()
    dari = models.CharField(max_length=30)
    untuk = models.CharField(max_length=30)
    keterangan = models.CharField(max_length=100)
    pemasukan = models.CharField(max_length=200)
    pengeluaran = models.CharField(max_length=200)
 
    def __str__(self):
        return str(self.id)
    
    class Meta:
        db_table = "Kas"


