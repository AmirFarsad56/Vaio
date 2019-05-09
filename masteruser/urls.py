from django.urls import include, path
from masteruser.views import (MasterUserSignupView, MasterUserListView,
                              MasterUserBanView,MasterUserUnBanView,
                              MasterUserDeleteView,MasterUserProfileView,
                              BannedMasterUserListView, MasterUserDetailView,
                              MesssageSendingView, EmailSendingView)

app_name ='masteruser'
urlpatterns = [
    path('signup/', MasterUserSignupView, name='signup'),
    path('profile/<slug:slug>', MasterUserProfileView, name='profile'),
    path('list/', MasterUserListView.as_view(), name='list'),
    path('bannedlist/', BannedMasterUserListView.as_view(), name='bannedlist'),
    path('<slug:slug>/ban/',MasterUserBanView, name='ban'),
    path('<slug:slug>/unban/',MasterUserUnBanView, name='unban'),
    path('<slug:slug>/delete/',MasterUserDeleteView, name='delete'),
    path('detail/<slug:slug>/',MasterUserDetailView, name='detail'),
    path('sendsms/<slug:slug>/',MesssageSendingView, name='sendsms'),
    path('sendemail/<slug:slug>/',EmailSendingView, name='sendemail'),

]
