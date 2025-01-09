from django.contrib import admin

# Register your models here.
from .models import Dbsurat

class Surat(admin.ModelAdmin):
    list_display = ( "id", 'nama', 'surat', 'trak', "tgl" ,"jam" ,"tentang", "upload_file"  )
    search_fields = ('nama', 'surat' , "trak" )


admin.site.register(Dbsurat,Surat )
