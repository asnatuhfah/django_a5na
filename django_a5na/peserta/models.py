from django.db import models

# Create your models here.
class Pekerjaan(models.Model):
    posisi = models.CharField(max_length=100)
    perusahaan = models.CharField(max_length=100)

    def __str__(self):
        return self.posisi

    class Meta:
        db_table = 'pekerjaan'
        ordering = ['id']

class Peserta (models.Model):
    PILIHAN_GENDER = (
        ('Pria','Pria'),
        ('Wanita','Wanita'),
        ('Waria','Waria')

    )
    nama =models.CharField (max_length=100)
    gender =models.CharField (max_length=10, choices=PILIHAN_GENDER)
    no_hp =models.CharField (max_length=15)
    usia =models.CharField (max_length=3, blank=True, null=True)
    alamat =models.CharField (max_length=255)
    pekerjaan = models.ForeignKey(
        Pekerjaan, on_delete=None, related_name='pesertas', null=True)
    hobi =models.CharField (max_length=100, blank=True, null=True)


    
    class Meta:
        db_table ='peserta'
        ordering =['id']