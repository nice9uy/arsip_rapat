from django.urls import path
from . import views

urlpatterns = [
     path('', views.home, name='home' ),
     path('tambah_data/', views.tambah_data, name='tambah_data' ),
     path('tambah_data_surat/', views.tambah_data_surat, name='tambah_data_surat' ),

     path('dashboard/', views.dashboard, name='dashboard' ),
     path('kas/', views.kas, name='kas' ),
     path('kas_pemasukan/<int:id_kas_masuk>/', views.kas_pemasukan, name='kas_pemasukan' ),
     path('kas_pengeluaran/<int:id_kas_keluar>/', views.kas_pengeluaran, name='kas_pengeluaran' ),

     path('cari_tgl_rapat/', views.cari_tgl_rapat, name='cari_tgl_rapat' ),
     # path('laporan/', views.laporan, name='laporan' ),

     # path('dashboard_edit/<int:id_dashboard_katagori_edit>', views.dashboard_edit, name='dashboard_edit' ),
     # path('dashboard_delete/<int:id_dashboard_katagori_delete>', views.dashboard_delete, name='dashboard_delete' ),

     # path('setting_katagori/', views.setting_katagori, name='setting_katagori'),
     # path('setting_katagori_add/', views.setting_katagori_add, name='setting_katagori_add'),
     # path('setting_katagori_edit/<int:id_setting_katagori_edit>', views.setting_katagori_edit, name='setting_katagori_edit'),
     # path('setting_katagori_delete/<int:id_setting_katagori_delete>', views.setting_katagori_delete, name='setting_katagori_delete'),
]