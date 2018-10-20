from django.contrib import admin
from peserta.models import Peserta, Pekerjaan

# Register your models here.
class PesertaAdmin(admin.ModelAdmin):
    model =Peserta
    list_display = ['nama','gender','no_hp','usia','alamat']

class PekerjaanAdmin(admin.ModelAdmin):
    model =Pekerjaan
    list_display = ['posisi','perusahaan']

admin.site.register(Peserta, PesertaAdmin)
admin.site.register(Pekerjaan, PekerjaanAdmin)

