from django import forms
from peserta.models import Pekerjaan, Peserta


class PesertaForm(forms.Form):
    PILIHAN_GENDER = (
        ('Pria', 'Pria'),
        ('Wanita', 'Wanita')
    )

    pekerjaan_queryset = Pekerjaan.objects.all()

    id = forms.IntegerField(widget=forms.HiddenInput())
    nama = forms.CharField(max_length=100)
    gender = forms.ChoiceField(choices=PILIHAN_GENDER)
    no_hp = forms.CharField(max_length=15)
    usia = forms.CharField(max_length=3, required=False)
    alamat = forms.CharField(max_length=255)
    pekerjaan = forms.ModelChoiceField(queryset=pekerjaan_queryset)
    hobi = forms.CharField(max_length=100, required=False)

    class Meta:
        model = Peserta

class PekerjaanForm(forms.Form):
    
    
    id = forms.IntegerField(widget=forms.HiddenInput())
    posisi = forms.CharField(max_length=100)
    perusahaan = forms.CharField(max_length=100)
    

    class Meta:
        model = Pekerjaan
