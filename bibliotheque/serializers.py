# Ce projet a été réalisé par:
# - NDOUR Ndeye Aida
# - DJAKOPO Abiola David
# - BALDE Mamadou Saliou
# - BISSOMBOLO Siega
from rest_framework import serializers 
from bibliotheque.models import Book
 
 
class BookSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Book
        fields = ('id',
                  'titre',
                  'auteur',
                  'description',
                  #'prix'
                  )