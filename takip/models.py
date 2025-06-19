from django.db import models

# Create your models here.
class StokTanim(models.Model):
    stok_adi = models.CharField(max_length=100)
    stok_kodu = models.CharField(max_length=100)
    stok_mstr_kodu = models.CharField(max_length=100)
    stok_miktar = models.IntegerField()
    stok_birim = models.CharField(max_length=100)
    firma = models.ForeignKey(Firma, on_delete=models.CASCADE)


class StokHareket(models.Model):
    stok_kodu = models.ForeignKey(StokTanim, on_delete=models.CASCADE)
    stok_hareket_miktar = models.IntegerField()
    stok_hareket_birim = models.CharField(max_length=100)
    foto = models.ForeignKey(StokFotolar, on_delete=models.CASCADE)


class StokFotolar(models.Model):
    stok_kodu = models.ForeignKey(StokTanim, on_delete=models.CASCADE)
    stok_foto = models.ImageField(upload_to='stok_fotolar')

class Firma(models.Model):
    firma_adi = models.CharField(max_length=100)