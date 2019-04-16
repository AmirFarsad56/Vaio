from django.contrib import admin
from salon.models import SalonModel, SalonPictureModel

class SalonPictureModelInline(admin.StackedInline):
    model = SalonPictureModel
    can_delete = True
    verbose_name_plural = 'SalonPictureModel'
    fk_name = 'salon'

class SalonAdmin(admin.ModelAdmin):
    inlines = [SalonPictureModelInline,]


admin.site.register(SalonModel,SalonAdmin)
