from django.urls import include, path
from accounts.views import SuperUserProfileView

app_name ='accounts'
urlpatterns = [
    path('profile/<slug:slug>/', SuperUserProfileView.as_view(), name='profile'),

]
