from django.urls import include, path
from django.contrib.auth.views import LoginView, LogoutView
'''
app_name ='accounts'
urlpatterns = [
    path('login/',LoginView.as_view(template_name = 'accounts/login.html'),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('',include('django.contrib.auth.urls'))
]
'''