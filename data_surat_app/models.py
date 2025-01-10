from django.db import models

# Create your models here.

class Dbsurat(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    tgl = models.DateField()
    nama = models.CharField(max_length=30)
    surat = models.CharField(max_length=35)
    trak = models.CharField(max_length=35)
    jam = models.CharField(max_length=200)
    pemasukan = models.IntegerField(null=True, blank=True , default=0)
    pengeluaran = models.IntegerField(null=True, blank=True , default=0) 
    upload_file = models.FileField(upload_to='')
 
    def __str__(self):
        return str(self.id)
    
    class Meta:
        db_table = "Dbsurat"



