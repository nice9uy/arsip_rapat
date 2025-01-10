from django.contrib import admin

# Register your models here.
from .models import Dbsurat
# from .models import Kas

class Surat(admin.ModelAdmin):
    list_display = ( "id", 'nama', 'surat', 'trak', "tgl" ,"jam" , "pemasukan" , "pengeluaran"  , "upload_file"  )
    search_fields = ('nama', 'surat' , "trak" )

# class KasDatin(admin.ModelAdmin):
#     list_display = ( "id", 'tgl', 'dari', 'untuk', "keterangan" ,"pemasukan" ,"pengeluaran" )
#     search_fields = ('tgl', 'dari' , "untuk" , "keterangan" )


admin.site.register(Dbsurat,Surat )
# admin.site.register(Kas,KasDatin )

