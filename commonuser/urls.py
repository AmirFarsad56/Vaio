from django.urls import include, path
from commonuser.views import CommonUserSignupView, CommonUserProfileView

app_name ='commonuser'
urlpatterns = [
    path('commonuser/signup/', CommonUserSignupView, name='signup'),
    path('commonuser/profile/<slug:slug>/',CommonUserProfileView.as_view(),
         name = 'profile'),
]
