from django.contrib import admin
from session.models import SessionModel, LastDataModel


admin.site.register(SessionModel)
admin.site.register(LastDataModel)
