from datetime import date
from django.shortcuts import render,redirect,get_object_or_404
from . models import Dbsurat
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
import pandas as pd

# Create your views here.
def home(request):
    dbsurat = Dbsurat.objects.all()
    context =  { 
        'page_title' : 'Home',
        'dbsurat' : dbsurat
    }
    return render(request, "pages/index.html", context)

@csrf_protect
@login_required(login_url="/accounts/login/")
def dashboard(request):
    today = date.today() 
    dbsurat = Dbsurat.objects.filter( tgl = today )

    user = request.user
    groups = [group.name for group in user.groups.all()]
    groups_name = ', '.join(groups)


    context =  { 
        'page_title'    : 'Dashboard',
        'dbsurat'       : dbsurat,
        'group'         : groups_name,
     }
    return render(request, "pages/dashboard.html", context)

@login_required(login_url="/accounts/login/")
def tambah_data(request):
    dbsurat = Dbsurat.objects.all()

    user = request.user
    groups = [group.name for group in user.groups.all()]
    groups_name = ', '.join(groups)

    context =  { 
        'page_title'    : 'Dashboard',
        'dbsurat'       : dbsurat,
        'group'         : groups_name
    }
    return render(request, "pages/tambah_data.html", context)


@login_required(login_url="/accounts/login/")
def kas(request):

    kas = []  
    try:
        db_kas = Dbsurat.objects.all()

        if db_kas.exists():
            df_kas = pd.DataFrame(list(db_kas.values()))

            df_kas.loc[0,'saldo'] = df_kas.loc[0,'pemasukan'] - df_kas.loc[0,'pengeluaran']
            df_kas['saldo'] = df_kas['saldo'] + (df_kas['pemasukan'] + df_kas['pengeluaran']).shift(fill_value=0)

            for i in range(1, len(df_kas)):
                df_kas.loc[i, 'saldo'] = df_kas.loc[i-1, 'saldo'] + (df_kas.loc[i, 'pemasukan'] - df_kas.loc[i, 'pengeluaran'])
        
            kas = df_kas.to_dict(orient='records')  
        else:
            kas = []

    except Exception as e:
        print(f"Error: {e}")

    
    user = request.user
    groups = [group.name for group in user.groups.all()]
    groups_name = ', '.join(groups)

    context =  { 
        'page_title'    : 'KAS',
        'data_kas'       : kas,
        'group'         : groups_name
    }
    return render(request, "pages/kas.html", context)

@login_required(login_url="/accounts/login/")
def kas_pemasukan(request , id_kas_masuk ):

    kas_masuk = get_object_or_404(Dbsurat, pk = id_kas_masuk)
    
    if request.method == 'POST':

        get_tgl = request.POST.get('tgl')
        get_nama = request.POST.get('nama')
        get_surat = request.POST.get('surat')
        get_trak = request.POST.get('trak')
        get_jam = request.POST.get('jam')
        get_pemasukan =  request.POST.get('pemasukan')
        get_pengeluaran =  request.POST.get('pengeluaran')
        upload_file_rapat = request.FILES.get('file_name')


        data_data_rapat =  kas_masuk.upload_file.name
       
        if upload_file_rapat == None:
            upload_file = data_data_rapat

        else:
            upload_file = upload_file_rapat
            kas_masuk.upload_file.delete()

        kas_masuk = Dbsurat(
                id          = id_kas_masuk,
                tgl         = get_tgl,
                nama        = get_nama,
                surat       = get_surat,
                trak        = get_trak,
                jam         = get_jam,
                pemasukan   = get_pemasukan,
                pengeluaran = get_pengeluaran,
                upload_file = upload_file
            )
        kas_masuk.save()

        return redirect('kas')   



@login_required(login_url="/accounts/login/")
def kas_pengeluaran(request , id_kas_keluar ):

    kas_keluar = get_object_or_404(Dbsurat, pk = id_kas_keluar)
    
    if request.method == 'POST':

        get_tgl = request.POST.get('tgl')
        get_nama = request.POST.get('nama')
        get_surat = request.POST.get('surat')
        get_trak = request.POST.get('trak')
        get_jam = request.POST.get('jam')
        get_pemasukan =  request.POST.get('pemasukan')
        get_pengeluaran =  request.POST.get('pengeluaran')
        upload_file_rapat = request.FILES.get('file_name')


        data_data_rapat =  kas_keluar.upload_file.name
       
        if upload_file_rapat == None:
            upload_file = data_data_rapat

        else:
            upload_file = upload_file_rapat
            kas_keluar.upload_file.delete()

        kas_keluar = Dbsurat(
                id          = id_kas_keluar,
                tgl         = get_tgl,
                nama        = get_nama,
                surat       = get_surat,
                trak        = get_trak,
                jam         = get_jam,
                pemasukan   = get_pemasukan,
                pengeluaran = get_pengeluaran,
                upload_file = upload_file
            )
        kas_keluar.save()
        return redirect('kas')   


@csrf_protect
@login_required(login_url="/accounts/login/")
def tambah_data_surat(request):

    get_tgl = request.POST.get('tanggal')
    get_nama = request.POST.get('nama')
    get_no_surat = request.POST.get('no_surat')
    get_no_kontrak = request.POST.get('no_kontrak')
    get_jam = request.POST.get('jam')

    files_upload = request.FILES.get('file_name')

    upload_data = Dbsurat(
            tgl         = get_tgl,
            nama        = get_nama,
            surat       = get_no_surat,
            trak        = get_no_kontrak,
            jam         = get_jam,
            pemasukan   = 0,
            pengeluaran = 0,
            upload_file = files_upload,
        )
    upload_data.save()
    return redirect('dashboard')        
