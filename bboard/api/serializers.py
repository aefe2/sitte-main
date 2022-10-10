from rest_framework import serializers
from main.models import Bb

class BbSerializer(serializers.ModelSerializer):
   class Meta:
       model = Bb
       fields = ('id', 'title', 'content', 'price', 'created_at')
# страница 74