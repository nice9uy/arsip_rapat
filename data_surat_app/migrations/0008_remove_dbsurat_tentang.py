# Generated by Django 4.2.6 on 2025-01-10 00:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_surat_app', '0007_alter_kas_pemasukan_alter_kas_pengeluaran'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dbsurat',
            name='tentang',
        ),
    ]
