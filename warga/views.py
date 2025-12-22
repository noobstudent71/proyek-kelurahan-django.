from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Warga, Pengaduan
from .forms import WargaForm, PengaduanForm

# --- IMPOR DRF ---
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from .serializers import WargaSerializer, PengaduanSerializer

# ===========================
#        API VIEWS
# ===========================

class WargaViewSet(viewsets.ModelViewSet):
    queryset = Warga.objects.all().order_by('-tanggal_registrasi')
    serializer_class = WargaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    # Fitur Lanjutan
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['nama_lengkap', 'nik', 'alamat']
    ordering_fields = ['nama_lengkap', 'tanggal_registrasi']


class PengaduanViewSet(viewsets.ModelViewSet):
    queryset = Pengaduan.objects.all()
    serializer_class = PengaduanSerializer

    permission_classes = [IsAdminUser]
    
    # --- JAWABAN TANTANGAN ---
    # Menambahkan fitur pencarian dan pengurutan pada Pengaduan
    filter_backends = [SearchFilter, OrderingFilter]
    
    # Bisa mencari berdasarkan Judul atau Isi Deskripsi
    search_fields = ['judul', 'deskripsi']
    
    # Bisa mengurutkan berdasarkan Status atau Judul
    ordering_fields = ['status', 'judul']


# ===========================
#    HTML VIEWS (DJANGO)
# ===========================

class WargaListView(ListView):
    model = Warga

class WargaDetailView(DetailView):
    model = Warga

class PengaduanListView(ListView):
    model = Pengaduan

class WargaCreateView(CreateView):
    model = Warga
    form_class = WargaForm
    template_name = 'warga/warga_form.html'
    success_url = reverse_lazy('warga-list') 

class PengaduanCreateView(CreateView):
    model = Pengaduan
    form_class = PengaduanForm
    template_name = 'warga/pengaduan_form.html'
    success_url = reverse_lazy('pengaduan-list') 

class WargaUpdateView(UpdateView):
    model = Warga
    form_class = WargaForm
    template_name = 'warga/warga_form.html'
    success_url = reverse_lazy('warga-list')

class WargaDeleteView(DeleteView):
    model = Warga
    template_name = 'warga/warga_confirm_delete.html'
    success_url = reverse_lazy('warga-list')

class PengaduanUpdateView(UpdateView):
    model = Pengaduan
    form_class = PengaduanForm
    template_name = 'warga/pengaduan_form.html'
    success_url = reverse_lazy('pengaduan-list')

class PengaduanDeleteView(DeleteView):
    model = Pengaduan
    template_name = 'warga/pengaduan_confirm_delete.html'
    success_url = reverse_lazy('pengaduan-list')