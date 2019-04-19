from django.urls import include, path
from sportclub.views import SportClubSignupView, SportClubProfileView
from salon.views import SalonCreateView

app_name ='sportclub'
urlpatterns = [
    path('sportclub/signup/', SportClubSignupView, name='signup'),
    path('sportclub/profile/<slug:slug>/',SportClubProfileView,
         name='profile'),

]
