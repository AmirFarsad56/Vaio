from django.urls import include, path
from session.views import (SessionCreateView, SessionListView)

app_name ='session'
urlpatterns = [
    path('create/<int:pk>/', SessionCreateView, name='create'),
    path('list/<int:pk>/', SessionListView, name='list'),

]
