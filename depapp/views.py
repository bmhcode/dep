from django.shortcuts import render
from .models import Infos, Service, Subdivision, AppelsOffre, SecteurActivité, Projet, OffreEmploi, Bet, Entreprise

def index(request):
    infos        = Infos.objects.get(id=1)
    # infos      = Infos.objects.all()
    services     = Service.objects.all()
    subdivisions = Subdivision.objects.all()
    appelsOffres = AppelsOffre.objects.all()
    OffresEmplois = OffreEmploi.objects.filter(afficher=True)
    bets = Bet.objects.filter(afficher=True)
    etps = Entreprise.objects.filter(afficher=True)
    secteursActivités = SecteurActivité.objects.all()

    sect = request.GET.get('secteur')
    if sect == None:
        projets = Projet.objects.all()    
    else:
        projets = Projet.objects.filter(secteur__name = sect )
  
    context = { 'infos' : infos, 'services' : services, 'subdivisions': subdivisions,
                'appelsOffres': appelsOffres, 'secteursActivités' : secteursActivités,
                'projets' : projets , 'OffresEmplois' : OffresEmplois, 'bets': bets, 'etps': etps
                }
    
    return render(request,'index.html', context)



