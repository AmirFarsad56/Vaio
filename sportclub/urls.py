from django.urls import include, path
from sportclub.views import (SportClubSignupView, SportClubProfileView,
                            SportClubListView, SportClubDetailView,
                            BannedSportClubListView, SportClubBanView,
                            SportClubDeleteView,SportClubUnBanView)
from salon.views import SalonCreateView

app_name ='sportclub'
urlpatterns = [
    path('sportclub/signup/', SportClubSignupView, name='signup'),
    path('sportclub/profile/<slug:slug>/',SportClubProfileView,
         name='profile'),
    path('sportclub/list/', SportClubListView.as_view(), name='list'),
    path('sportclub/bannedlist/', BannedSportClubListView.as_view(),
         name='bannedlist'),
    path('sportclub/list/<slug:slug>/', SportClubDetailView, name='detail'),
    path('sportclub/ban/<slug:slug>/', SportClubBanView, name='ban'),
    path('sportclub/unban/<slug:slug>/', SportClubUnBanView, name='unban'),
    path('sportclub/delete/<slug:slug>/', SportClubDeleteView, name='delete'),


]
