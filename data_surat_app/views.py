from datetime import date
from django.shortcuts import render,redirect,get_object_or_404
from . models import Dbsurat, Kas 
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

    kas = []  # Inisialisasi kas sebagai list kosong
    try:
        # Ambil data dari model Kas
        db_kas = Kas.objects.all()

        # Periksa apakah queryset tidak kosong
        if db_kas.exists():
            df_kas = pd.DataFrame(list(db_kas.values()))

            # Menambahkan kolom 'saldo' jika data ada
            df_kas['saldo'] = df_kas['pemasukan'] - df_kas['pengeluaran']

            # Menambahkan saldo dengan pergeseran
            df_kas['saldo'] = df_kas['saldo'] + (df_kas['pemasukan'] + df_kas['pengeluaran']).shift( fill_value=0)
        
            kas = df_kas.to_dict(orient='records')  # Mengubah ke bentuk list of dicts
        else:
            # Jika tidak ada data, set kas ke list kosong
            kas = []

    except Exception as e:
        # Tangani error jika ada
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
def kas_pemasukan(request):
    
    get_tgl = request.POST.get('tgl')
    get_dari = request.POST.get('dari')
    get_keterangan = request.POST.get('ket')
    get_pemasukan = request.POST.get('pemasukan')

    print(get_tgl)
    print(get_dari)
    print(get_keterangan)
    print(get_pemasukan)

    pemasukan = Kas(
            tgl         = get_tgl,
            dari        = get_dari,
            untuk       = "-",
            keterangan  = get_keterangan,
            pemasukan   = get_pemasukan,
            pengeluaran = 0
        )
    pemasukan.save()

    return redirect('kas')   



@login_required(login_url="/accounts/login/")
def kas_pengeluaran(request):

    get_tgl = request.POST.get('tgl')
    get_untuk = request.POST.get('untuk')
    get_keterangan = request.POST.get('ket')
    get_pengeluaran = request.POST.get('pengeluaran')

    pengeluaran = Kas(
            tgl         = get_tgl,
            dari        = "-",
            untuk        = get_untuk,
            keterangan  = get_keterangan,
            pemasukan   = 0,
            pengeluaran   = get_pengeluaran,
        )
    
    print(pengeluaran)
    pengeluaran.save()

    return redirect('kas') 

@csrf_protect
@login_required(login_url="/accounts/login/")
def tambah_data_surat(request):

    get_nama = request.POST.get('nama')
    get_no_surat = request.POST.get('no_surat')
    get_no_kontrak = request.POST.get('no_kontrak')
    get_tanggal = request.POST.get('tanggal')
    get_jam = request.POST.get('jam')
    get_tentang = request.POST.get('tentang')

    files_upload = request.FILES.get('file_name')

    upload_data = Dbsurat(
            nama        = get_nama,
            surat       = get_no_surat,
            trak        = get_no_kontrak,
            tgl         = get_tanggal,
            jam         = get_jam,
            tentang     = get_tentang,
            upload_file = files_upload,
        )
    upload_data.save()
    return redirect('dashboard')        
