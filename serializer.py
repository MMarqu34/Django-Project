from rest_framework import serializer
from .models import user_reg

class user_regSerializer(serilizer.ModelSerializer):

    class Meta:
        model = user_reg
        fields = ('username','firstname','typeofuser')
        
