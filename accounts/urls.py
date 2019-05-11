from django.urls import include, path
from accounts.views import (SuperUserProfileView, SuperUserUpdateView,
                            CloudMessageView, CloudEmailView, PasswordChangeView)

app_name ='accounts'
urlpatterns = [
    path('profile/<slug:slug>/', SuperUserProfileView.as_view(), name='profile'),
    path('update/<slug:slug>/', SuperUserUpdateView, name='update'),
    path('cloudmessage/', CloudMessageView, name='cloudmessage'),
    path('cloudemail/', CloudEmailView, name='cloudemail'),
    path('passwordchange/<slug:slug>/', PasswordChangeView, name='passwordchange'),
]
