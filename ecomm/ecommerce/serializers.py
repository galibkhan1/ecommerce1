from pyexpat import model
from attr import field
from rest_framework import serializers
from .models import demodb

# class demo_rest(serializers.HyperlinkedModelSerializer):
class demo_rest(serializers.ModelSerializer):
    class Meta:
        model =demodb
        # fields = ('name','email')
        fields = '__all__'
