from django.urls import include, path
from salon.views import (SalonCreateView, SalonUpdateView, SalonDetailView,
                        PublishedSalonListView, UnPublishedSalonListView,
                        SalonConfirmView,)


app_name ='salon'
urlpatterns = [
    path('profile/<slug:slug>/createsalon/', SalonCreateView, name='createsalon'),
    path('publishedsalonlist/',PublishedSalonListView.as_view(),
        name='publishedsalonlist'),
    path('unpublishedsalonlist/',UnPublishedSalonListView.as_view(),
        name='unpublishedsalonlist'),
    path('sportclub/profile/<slug:slug>/updatesalon/<int:pk>/',SalonUpdateView.as_view(), name='updatesalon'),
    path('sportclub/profile/<slug:slug>/salondetail/<int:pk>/',SalonDetailView.as_view(), name='salondetail'),
    path('salon/confirm/<int:pk>/',SalonConfirmView, name='confirm'),

]
