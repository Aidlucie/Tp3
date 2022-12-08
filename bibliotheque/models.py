# Ce projet a été réalisé par:
# - NDOUR Ndeye Aida
# - DJAKOPO Abiola David
# - BALDE Mamadou Saliou
# - BISSOMBOLO Siega
from django.db import models

# Create your models here.
class Book(models.Model):
    titre = models.CharField(max_length=100, blank=False, default='')
    auteur = models.CharField(max_length=150,blank=False,default='')
    description = models.CharField(max_length=200,blank=False, default='')
   # prix = models.models.IntegerField()

