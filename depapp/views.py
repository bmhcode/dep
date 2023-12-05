from django.shortcuts import render
from .models import Infos, Service, Subdivision, AppelsOffre, SecteurActivité, Projet, OffreEmploi

def index(request):
    infos        = Infos.objects.get(id=1)
    # infos    = Infos.objects.all()
    services     = Service.objects.all()
    subdivisions = Subdivision.objects.all()
    appelsOffres = AppelsOffre.objects.all()
    secteursActivités = SecteurActivité.objects.all()
    projets       = Projet.objects.all()
    OffresEmplois = OffreEmploi.objects.filter(afficher=True)

    context = { 'infos' : infos, 'services' : services, 'subdivisions': subdivisions,
                'appelsOffres': appelsOffres, 'secteursActivités' : secteursActivités, 'projets' : projets , 'OffresEmplois' : OffresEmplois}
    
    return render(request,'index.html', context)


