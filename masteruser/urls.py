from django.urls import include, path
from masteruser.views import (MasterUserSignupView, MasterUserListView,
                              MasterUserBanView,MasterUserUnBanView,
                              MasterUserDeleteView,MasterUserProfileView)

app_name ='masteruser'
urlpatterns = [
    path('masteruser/signup/', MasterUserSignupView, name='signup'),
    path('masteruser/profile/<slug:slug>', MasterUserProfileView, name='profile'),    
    path('masteruser/list/', MasterUserListView.as_view(), name='list'),
    path('masteruser/list/<int:pk>/ban/',MasterUserBanView, name='ban'),
    path('masteruser/list/<int:pk>/unban/',MasterUserUnBanView, name='unban'),
    path('masteruser/list/<int:pk>/delete/',MasterUserDeleteView, name='delete'),

]
