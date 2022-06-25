from django.contrib import admin
from .models import *

class cascoAdmin(admin.ModelAdmin):
    list_display = ('marca', 'tipo', 'talle', 'precio')
class camperaAdmin(admin.ModelAdmin):
    list_display = ('marca', 'tipo', 'talle', 'precio')

class bolsoAdmin(admin.ModelAdmin):
    list_display = ('marca', 'tipo', 'talle', 'precio')

class guanteAdmin(admin.ModelAdmin):
    list_display = ('marca', 'tipo', 'talle', 'precio')

class pantalonAdmin(admin.ModelAdmin):
    list_display = ('marca', 'tipo', 'talle', 'precio')

admin.site.register (casco, cascoAdmin)
admin.site.register (campera, cascoAdmin)
admin.site.register (bolso, bolsoAdmin)
admin.site.register (guante, guanteAdmin)
admin.site.register (pantalon, pantalonAdmin)
