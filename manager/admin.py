from django.contrib import admin
from .models import Model_Master,Model_Link_Master,Model_Link_Detail, Util_Mgmt

class ManagerAdmin(admin.ModelAdmin):
  list_display = ('title', 'author', 'created',)
# Register your models here.
admin.site.register(Model_Master)
admin.site.register(Model_Link_Master)
admin.site.register(Model_Link_Detail)
admin.site.register(Util_Mgmt)



