from django.urls import include, path
from accounts.views import (SuperUserProfileView, SuperUserUpdateView,
                            CloudMessageView, CloudEmailView )

app_name ='accounts'
urlpatterns = [
    path('profile/<slug:slug>/', SuperUserProfileView.as_view(), name='profile'),
    path('update/<slug:slug>/', SuperUserUpdateView.as_view(), name='update'),
    path('cloudmessage/', CloudMessageView, name='cloudmessage'),
    path('cloudemail/', CloudEmailView, name='cloudemail'),

]
