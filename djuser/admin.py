from django.contrib import admin
from .models import Djuser
# Register your models here.


class DjuserAdmin(admin.ModelAdmin):
    list_display = ('email', )


admin.site.register(Djuser, DjuserAdmin)
