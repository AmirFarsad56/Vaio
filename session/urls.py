from django.urls import include, path
from session.views import (SessionCreateView, SessionListView, LengthError)

app_name ='session'
urlpatterns = [
    path('create/<int:pk>/', SessionCreateView, name='create'),
    path('list/<int:pk>/', SessionListView, name='list'),
    path('length-error', LengthError.as_view(), name='lengtherror'),
]
