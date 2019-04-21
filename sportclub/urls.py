from django.urls import include, path
from sportclub.views import (SportClubSignupView, SportClubProfileView,
                            SportClubListView, SportClubDetailView,
                            BannedSportClubListView, SportClubBanView,
                            SportClubDeleteView,SportClubUnBanView,
                            BannedSportClubExceptionView)
from salon.views import SalonCreateView

app_name ='sportclub'
urlpatterns = [
    path('signup/', SportClubSignupView, name='signup'),
    path('profile/<slug:slug>/', SportClubProfileView, name='profile'),
    path('list/', SportClubListView.as_view(), name='list'),
    path('bannedlist/', BannedSportClubListView.as_view(), name='bannedlist'),
    path('list/<slug:slug>/', SportClubDetailView, name='detail'),
    path('ban/<slug:slug>/', SportClubBanView, name='ban'),
    path('unban/<slug:slug>/', SportClubUnBanView, name='unban'),
    path('delete/<slug:slug>/', SportClubDeleteView, name='delete'),
    path('salon/bannedsportclub/<slug:slug>',BannedSportClubExceptionView,
         name='bannedsportclubexception'),


]
