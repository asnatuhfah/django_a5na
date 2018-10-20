from django.shortcuts import render, redirect
from django.views.generic import View
from peserta.forms import PesertaForm, PekerjaanForm
from django.http import HttpResponse
from peserta.models import Peserta, Pekerjaan
from django.contrib import messages

# Create your views here.

class IndexView(View):
    template_name = 'form_pendaftaran.html'

    def get(self, request):

        return render(request, self.template_name, {
            'form': PesertaForm(request.POST)
        })

    def post(self, request):
        form = PesertaForm(request.POST)
        if form.is_valid():
            peserta = Peserta()
            peserta.nama = form.cleaned_data['nama']
            peserta.gender = form.cleaned_data['gender']
            peserta.no_hp = form.cleaned_data['no_hp']
            peserta.usia = form.cleaned_data['usia']
            peserta.alamat = form.cleaned_data['alamat']
            peserta.pekerjaan = form.cleaned_data['pekerjaan']
            peserta.hobi = form.cleaned_data['hobi']
            peserta.save()

            messages.add_message(request, messages.INFO,
                                 "Pendaftaran berhasil!", extra_tags="success")
            return redirect('/peserta/index')
        else:
            return HttpResponse(form.errors)

class ListPendaftaranView(View):
    template_name = 'list_pendaftaran.html'

    def get(self, request):
        context_data = {
            'list_peserta': Peserta.objects.all()
        }
        return render(request, self.template_name, context_data)

class HapusPesertaView(View):
    def get(self, request, peserta_id):
        peserta =Peserta.objects.get(id=peserta_id)
        peserta.delete()
 
        messages.add_message(request, messages.INFO,
                                 "Oke Fine elu gua END", extra_tags="success")
        return redirect('peserta:list')


class UbahPesertaView(View):
    template_name = 'form_ubahpendaftaran.html'

    def get(self, request, peserta_id):
        peserta = Peserta.objects.get(id=peserta_id)
        
        initial_data = {
            'id': peserta.id,
            'nama': peserta.nama,
            'gender': peserta.gender,
            'alamat': peserta.alamat,
            'usia': peserta.usia,
            'no_hp': peserta.no_hp,
            'pekerjaan': peserta.pekerjaan,
            'hobi': peserta.hobi,
        }

        context_data = {
            'form': PesertaForm(initial=initial_data),
        }

        return render(request, self.template_name, context_data)

class UpdatePesertaView(View):
    def post(self, request):
        form = PesertaForm(request.POST)
        if form.is_valid():
            peserta_id = form.cleaned_data['id']

            peserta = Peserta.objects.get(id=peserta_id)
            peserta.nama = form.cleaned_data['nama']
            peserta.gender = form.cleaned_data['gender']
            peserta.no_hp = form.cleaned_data['no_hp']
            peserta.usia = form.cleaned_data['usia']
            peserta.alamat = form.cleaned_data['alamat']
            peserta.pekerjaan = form.cleaned_data['pekerjaan']
            peserta.hobi = form.cleaned_data['hobi']
            peserta.save()

            messages.add_message(request, messages.INFO,
                                 "Ubah pendaftaran berhasil!", extra_tags="success")
            return redirect('/peserta/list_pendaftaran')
        else:
            return HttpResponse(form.errors)
    
class PekerjaanView(View):
    template_name = 'form_pekerjaan.html'

    def get(self, request):

        return render(request, self.template_name, {
            'form': PekerjaanForm(request.POST)
        })

    def post(self, request):
        form = PekerjaanForm(request.POST)
        print (form.is_valid())
        if form.is_valid():
            Pekerjaan = Pekerjaan()
            Pekerjaan.posisi = form.cleaned_data['posisi']
            Pekerjaan.perusahaan = form.cleaned_data['perusahaan']
            Pekerjaan.save()

            messages.add_message(request, messages.INFO,
                                 "Pendaftaran berhasil!", extra_tags="success")
            return redirect('peserta:pekerjaan')
        else:
            return HttpResponse(form.errors)

class ListPekerjaanView(View):
    template_name = 'list_pekerjaan.html'

    def get(self, request):
        context_data = {
            'list_pekerjaan': Pekerjaan.objects.all()
        }
        return render(request, self.template_name, context_data)

class HapusPekerjaanView(View):
    def get(self, request, pekerjaan_id):
        pekerjaan =Pekerjaan.objects.get(id=pekerjaan_id)
        pekerjaan.delete()
 
        messages.add_message(request, messages.INFO,
                                 "Oke Fine elu gua END", extra_tags="success")
        return redirect('peserta:list_peker')

