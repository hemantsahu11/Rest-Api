from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Language, Paradigm, Programmer
from .serializers import LanguageSerializer, ParadigmSerializer, ProgrammerSerializer
# Create your views here.


def home(request):
    return HttpResponse("hello world")


class LanguageView(viewsets.ModelViewSet):    # viewsets model will take care of everything like request methods etc..
    queryset = Language.objects.all()           # this only view is sufficient for get, post , put , delete
    serializer_class = LanguageSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )  # user should be logged in otherwise he will be able to read only


class ParadigmView(viewsets.ModelViewSet):
    queryset = Paradigm.objects.all()
    serializer_class = ParadigmSerializer


class ProgrammerView(viewsets.ModelViewSet):
    queryset = Programmer.objects.all()
    serializer_class = ProgrammerSerializer

    # we can make the separate functions also inside class for separate get and post methods for example :-
    # def get(self, request, *args, **kwargs )
        # logic ..........


"""  ------------------ function based apis in django ------------------------------"""


@api_view()
def say_hello(request):
    return Response({"message": "Hello world "})


@api_view(['GET'])           # view for getting data of model
def get_data(request):
    languages = Language.objects.all()
    language_list = []
    for language in languages:
        language_dic = {"name": language.name}
        language_list.append(language_dic)
    return Response({"Languages": language_list})


# def get_data(request, methods=['GET']):   why this is not working
#     languages = Language.objects.all()
#     language_list = []
#     for language in languages:
#         language_dic = {"name": language.name}
#         language_list.append(language_dic)
#     return Response({"Languages": language_list})





