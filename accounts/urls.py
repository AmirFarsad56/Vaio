from django.urls import include, path
from accounts.views import SuperUserProfileView, SuperUserUpdateView

app_name ='accounts'
urlpatterns = [
    path('profile/<slug:slug>/', SuperUserProfileView.as_view(), name='profile'),
    path('update/<slug:slug>/', SuperUserUpdateView.as_view(), name='update'),

]
