from django.urls import include, path
from sportclub.views import SportClubSignupView, SportClubProfileView

app_name ='sportclub'
urlpatterns = [
    path('sportclub/signup/', SportClubSignupView, name='signup'),
    path('sportclub/profile/<int:pk>/',SportClubProfileView.as_view(),
         name='profile'),
]
