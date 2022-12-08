# Ce projet a été réalisé par:
# - NDOUR Ndeye Aida
# - DJAKOPO Abiola David
# - BALDE Mamadou Saliou
# - BISSOMBOLO Siega
from django.urls import re_path,include
#from django.conf.urls import url 
from bibliotheque import views

urlpatterns = [
    #path("", views.home, name="home"),
    # path("", views.home, name="home"),
    re_path(r'^api/bibliotheque$', views.book_list),
    re_path(r'^api/bibliotheque/(?P<pk>[0-9]+)$', views.book_detail),
   # re_path(r'^api/bibliotheque/published$', views.book_list_published)
]