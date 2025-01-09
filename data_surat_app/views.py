from datetime import date
from django.shortcuts import render,redirect,get_object_or_404
from . models import Dbsurat, Kas 
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator

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
    db_kas = Kas.objects.all()
    
    user = request.user
    groups = [group.name for group in user.groups.all()]
    groups_name = ', '.join(groups)

    context =  { 
        'page_title'    : 'KAS',
        # 'dbsurat'       : dbsurat,
        'group'         : groups_name
    }
    return render(request, "pages/kas.html", context)


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
