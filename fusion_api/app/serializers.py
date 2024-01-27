from rest_framework import serializers
from .models import *




class SneakersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Sneakers
        fields = '__all__'

class CommandeSerializers(serializers.ModelSerializer):
    class Meta : 
        model : Commandes
        fields = '__all__'