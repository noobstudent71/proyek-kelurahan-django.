from rest_framework import serializers
from .models import Warga,Pengaduan

class WargaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warga
        # Tentukan field dari model Warga yang ingin kita ekspos di API
        fields = ['id', 'nik', 'nama_lengkap', 'alamat', 'no_telepon']

class PengaduanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pengaduan
        # '__all__' artinya kita ambil semua field yang ada di model
        fields = '__all__'