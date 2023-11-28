from django.contrib import admin

from .models import Infos, Service, Subdivision, AppelsOffre,Entreprise,Bet,SecteurActivité,Projet,ProjetImages 

admin.site.register(Infos)
admin.site.register(Service)
admin.site.register(Subdivision)
admin.site.register(AppelsOffre)
admin.site.register(Entreprise)
admin.site.register(Bet)
admin.site.register(SecteurActivité)

class ProjetAdmin(admin.ModelAdmin):
  list_display = ("libellé", "secteur", "état",)

admin.site.register(Projet, ProjetAdmin)  
admin.site.register(ProjetImages)
