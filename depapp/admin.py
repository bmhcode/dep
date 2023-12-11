from django.contrib import admin

from .models import Infos, Service , Subdivision , AppelsOffre ,Entreprise ,Bet ,SecteurActivité ,Projet ,ProjetImages , OffreEmploi

class InfosAdmin(admin.ModelAdmin):
  list_display = ("name", "libellé", "directeur")
admin.site.register(Infos, InfosAdmin) 


class ServiceAdmin(admin.ModelAdmin):
  list_display = ("name", "chefService", "description")
admin.site.register(Service, ServiceAdmin)  

class SubdivisionAdmin(admin.ModelAdmin):
  list_display = ("name", "chefSubdivision", "telephone", "email")
admin.site.register(Subdivision, SubdivisionAdmin)  

admin.site.register(SecteurActivité)

class AppelsOffreAdmin(admin.ModelAdmin):
  list_display = ("type", "projet", "date_début", "date_fin", "afficher")
admin.site.register(AppelsOffre, AppelsOffreAdmin)  

class EntrepriseAdmin(admin.ModelAdmin):
  list_display = ("name", "contact", "mobile", "afficher",)
admin.site.register(Entreprise, EntrepriseAdmin)  

class BetAdmin(admin.ModelAdmin):
  list_display = ("name", "contact", "mobile", "afficher",)
admin.site.register(Bet, BetAdmin)  

class ProjetAdmin(admin.ModelAdmin):
  list_display = ("libellé", "secteur", "état","afficher")
admin.site.register(Projet, ProjetAdmin)  

admin.site.register(ProjetImages)

class OffreEmploiAdmin(admin.ModelAdmin):
  list_display = ("description", "afficher","date_début", "date_fin")
admin.site.register(OffreEmploi,OffreEmploiAdmin)
