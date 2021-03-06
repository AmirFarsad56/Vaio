from django.urls import include, path
from salon.views import (SalonCreateView, SalonUpdateView, SalonDetailView,
                        ConfirmedSalonListView, UnConfirmedSalonListView,
                        SalonConfirmView, SalonDeleteView, SalonBanView,
                        SalonDetailsView)


app_name ='salon'
urlpatterns = [
    path('profile/<slug:slug>/createsalon/', SalonCreateView, name='createsalon'),
    path('confirmedsalonlist/',ConfirmedSalonListView.as_view(),
        name='confirmedsalonlist'),
    path('unconfirmedsalonlist/',UnConfirmedSalonListView.as_view(),
        name='unconfirmedsalonlist'),
    path('sportclub/<slug:slug>/profile/updatesalon/<int:pk>/',SalonUpdateView, name='update'),
    path('sportclub/profile/salondetail/<int:pk>/',SalonDetailView.as_view(), name='salondetail'),
    path('salon/confirm/<int:pk>/',SalonConfirmView, name='confirm'),
    path('salon/delete/<int:pk>/',SalonDeleteView, name='delete'),
    path('salon/ban/<int:pk>/',SalonBanView, name='ban'),
    path('salon/detail/<int:pk>/',SalonDetailsView, name='detail'),

]
