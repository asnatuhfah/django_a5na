from django.urls import path
from peserta.views import IndexView, ListPendaftaranView, HapusPesertaView, UbahPesertaView, UpdatePesertaView, PekerjaanView, ListPekerjaanView, HapusPekerjaanView

app_name = 'peserta'

urlpatterns = [
    path('index', IndexView.as_view(), name='idx'),
    path('list_pendaftaran', ListPendaftaranView.as_view(), name='list'),
    path('hapus/<int:peserta_id>', HapusPesertaView.as_view(), name='hapus'),
    path('ubah/<int:peserta_id>', UbahPesertaView.as_view(), name='ubah'),
    path('update', UpdatePesertaView.as_view(), name='update'),
    path('pekerjaan', PekerjaanView.as_view(), name='pekerjaan'),
    path('list_pekerjaan', ListPekerjaanView.as_view(), name='listpeker'),
    path('hapus_pekerjaan/<int:pekerjaan_id>', HapusPekerjaanView.as_view(), name='hapus_pekerjaan'),

]