from django.db import models
from model_utils import Choices


class Infos(models.Model):
    name        = models.CharField(max_length=50, blank=False, null=False , default="DEP de Constntine", verbose_name="Dénomination" )
    libellé     = models.CharField(max_length=120, blank=True, null=True )
    description = models.TextField(blank=True, null=True )
    adresse     = models.CharField(max_length=120,blank=True, null=True )
    telephone   = models.CharField(max_length=30, blank=True, null=True )
    fax         = models.CharField(max_length=12, blank=True, null=True )
    email       = models.CharField(max_length=35, blank=True, null=True )
    image1      = models.ImageField(upload_to='Direction/', blank=True, null=False)
    image2      = models.ImageField(upload_to='Direction/', blank=True, null=False)
    
    directeur = models.CharField(max_length=50, default='Mr : Directeur', blank=True, null=True )
    directeurImage = models.ImageField(upload_to='Direction/', blank=True, null=False, verbose_name="Photo du Directeur" )
    directeurInformations = models.TextField( blank=True, null=True, verbose_name="Informations " )

    OpérationsInscrite = models.PositiveIntegerField(default=0)
    personnel = models.PositiveIntegerField(default=0)
   
    def __str__(self):
        return self.name
    
    class metat:
        # ordering = [""]
        verbos_name = "Informations"
        verbos_name_plural = "Informations"


class Service(models.Model):
    name        = models.CharField(max_length=100)
    chefService = models.CharField(max_length=50, default='Chef de Service')
    photo       = models.ImageField(upload_to='Chef_Service/', blank=True, null=False)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Subdivision(models.Model):
    name      = models.CharField(max_length = 100)
    chefSubdivision = models.CharField(max_length = 50, default='Chef de Subdivision')
    telephone = models.CharField(max_length = 30, default="031 31 31 31")
    email     = models.CharField(max_length = 35, default="Email")
   
    def __str__(self):
        return self.name
    
class AppelsOffre(models.Model):
    TYPE_APPEL = Choices(
        ("Appel d'offre","Appel d'offre"),
        ("Consultation","Consultation"),
        ("Grie a Grie","Grie a Grie"),
    )
    type = models.CharField(max_length=20, choices = TYPE_APPEL, default="Appel d'offre")
    projet = models.TextField()
    date_début = models.DateField(blank=True, null=True )
    date_fin = models.DateField(blank=True, null=True )
   
    def __str__(self):
        return self.type

class Entreprise(models.Model):
    name      = models.CharField(max_length=100)
    logo      = models.ImageField(upload_to='Entreprise/', blank=True, null=False)
    telephone = models.CharField(max_length = 30,blank=True, null=True )
    email     = models.CharField(max_length = 35,blank=True, null=True )
    contact   = models.CharField(max_length = 50, blank=True, null=True )
    mobile    = models.CharField(max_length = 30,blank=True, null=True )
    observation = models.TextField(blank=True, null=True )
    active = models.BooleanField(default=True)

class Bet(models.Model):
    name      = models.CharField(max_length=100) 
    logo      = models.ImageField(upload_to='BET/', blank=True, null=False)
    telephone = models.CharField(max_length=30,blank=True, null=True )
    email     = models.CharField(max_length=35,blank=True, null=True )
    contact   = models.CharField(max_length=50, blank=True, null=True )
    mobile    = models.CharField(max_length=30,blank=True, null=True )
    observation = models.TextField(blank=True, null=True )
    active = models.BooleanField(default=True)


class SecteurActivité(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="Secteurs d'activité/", blank=True, null=False)
    nombreProjets = models.PositiveIntegerField(default=0, blank=True, null=True )
    afficher = models.BooleanField(default=True)
    afficherDroite = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Projet(models.Model):
    ETAT_PROJET = Choices(
        ('Récent','Récent'),
        ('En cours','En cours'),
        ('Achevé','Achevé'),
    )

    libellé   = models.CharField("Libellé du projet", max_length=100, blank=False, null=False )
    état    = models.CharField("Etat du projet", max_length=20, choices = ETAT_PROJET , default='Récent')
    secteur = models.ForeignKey(SecteurActivité,related_name="Secteurs",on_delete=models.CASCADE, verbose_name="Secteur d'activité")
    image   = models.ImageField(upload_to='Projets/', blank=True, null=False)
    description = models.TextField(blank=True, null=True )
    afficher    = models.BooleanField(default=True)

    def __str__(self):
        return self.libellé

class ProjetImages(models.Model):
    projet = models.ForeignKey(Projet,related_name="Images",on_delete=models.CASCADE)
    image= models.ImageField(upload_to='Projets/Images/', blank=True, null=False)
    description = models.TextField(blank=True, null=True )
    afficher = models.BooleanField(default=True)

    # def __str__(self):
    #     return self.name
    # class Meta:
    #     verbose_plurial_name = "Images du projet"
