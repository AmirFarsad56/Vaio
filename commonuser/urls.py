from django.urls import include, path
from commonuser.views import (CommonUserSignupView, CommonUserProfileView,
                              CommonUserListView, CommonUserBanView,
                              CommonUserUnBanView, CommonUserDetailView,
                              CommonUserDeleteView, BannedCommonUserListView,
                              MesssageSendingView, EmailSendingView)

app_name ='commonuser'
urlpatterns = [
    path('signup/', CommonUserSignupView, name='signup'),
    path('profile/<slug:slug>/',CommonUserProfileView.as_view(),
         name = 'profile'),
    path('list/', CommonUserListView.as_view(), name='list'),
    path('bannedlist/', BannedCommonUserListView.as_view(), name='bannedlist'),
    path('list/<slug:slug>/', CommonUserDetailView, name='detail'),
    path('ban/<slug:slug>/', CommonUserBanView, name='ban'),
    path('unban/<slug:slug>/', CommonUserUnBanView, name='unban'),
    path('delete/<slug:slug>/', CommonUserDeleteView, name='delete'),
    path('sendsms/<slug:slug>/',MesssageSendingView, name='sendsms'),
    path('sendemail/<slug:slug>/',EmailSendingView, name='sendemail'),

]
