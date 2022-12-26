from rest_framework import serializers
from .models import Language, Paradigm, Programmer


class LanguageSerializer(serializers.ModelSerializer):   # this class will take care of converting data to json and json to data
    class Meta:
        model = Language
        fields = ['id', 'name', 'paradigm']


class ParadigmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paradigm
        fields = ['id', 'name']


class ProgrammerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programmer
        fields = ['id', 'name', 'languages']