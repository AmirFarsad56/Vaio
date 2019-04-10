from django.urls import include, path
from salon.views import SalonCreateView, SalonUpdateView, SalonDetailView


app_name ='salon'
urlpatterns = [
    path('createsalon/', SalonCreateView, name='createsalon'),
    path('updatesalon/<int:pk>/',SalonUpdateView.as_view(), name='updatesalon'),
    path('salondetail/<int:pk>/',SalonDetailView.as_view(), name='salondetail'),


]
