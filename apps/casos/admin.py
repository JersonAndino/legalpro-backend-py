from django.contrib import admin
from apps.casos.models import CasoTipo

# Register your models here.
class CasoTipoAdmin(admin.ModelAdmin):
    list_display = ('id', 'codigo', 'nombre', 'descripcion')  # Fields to show in the list view
    search_fields = ('nombre', 'codigo')  # Enables search by 'nombre'
    # list_filter = ('activo', 'fecha_creacion')  # Adds filters on the right panel
    ordering = ('-id',)  # Orders cases by newest first
    
admin.site.register(CasoTipo, CasoTipoAdmin)