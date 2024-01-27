from django.db import models

# Create your models here.



class Brand(models.Model):
    nom = models.CharField(max_length = 100)
    def __str__(self):
        return self.nom
    

class Sneakers(models.Model):
    categories = (('femme','femme'),('homme','homme'),('enfant','enfant'),('bebe','bébé'))
    image = models.ImageField(upload_to="images/" , blank=True , null=True) 
    #colors
    nom = models.CharField(max_length = 150)
    pointure = models.FloatField()
    prix = models.IntegerField(blank=True , null=True)
    description = models.CharField(max_length=500 , blank=True , null=True)
    category = models.CharField(max_length = 20 , choices = categories)
    ready_now = models.BooleanField(blank=True , null=True)

    def __str__(self):
        return self.nom
    @property
    def get_image_url(self) -> str:
      if self.image_file and hasattr(self.image_file, 'url'):
         return f"http://localhost:8000{self.image_file.url}"
    
class Commandes(models.Model):
    nom = models.CharField(max_length = 250)
    prenom = models.CharField(max_length = 250)
    adress = models.CharField(max_length = 200)
    phone_number = models.CharField(max_length = 10)
    email = models.EmailField(null = True)
    shoe = models.ForeignKey('Sneakers' , on_delete = models.CASCADE)

    def __str__(self):
        return self.nom