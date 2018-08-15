from django.contrib import admin
from .models import ModelMaster,ModeLinkMaster,ModeLinkDetail, UtilMgmt

class ManagerAdmin(admin.ModelAdmin):
  list_display = ('title', 'author', 'created',)
# Register your models here.
admin.site.register(ModelMaster)
admin.site.register(ModeLinkMaster)
admin.site.register(ModeLinkDetail)
admin.site.register(UtilMgmt)



