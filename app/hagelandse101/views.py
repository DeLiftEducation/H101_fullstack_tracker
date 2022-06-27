import os
from array import array
from encodings import utf_8
from turtle import position
from django.shortcuts import render
import json
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.core import serializers
from django.http import JsonResponse
from hagelandse101.models import DatacollectorParticipation, DatacollectorPerson, DatacollectorPosition, DatacollectorEdition



def index(request):
    
    with open('hagelandse101/static/route.json', 'r', encoding='utf_8') as f:
        routejson = json.load(f)
    
    
    edities = DatacollectorEdition.objects.all()
    request.session["edition"] = 0
    deelnemers = DatacollectorPerson.objects.all()
    
    

    context = {
        'routejson': routejson,
        'deelnemers': deelnemers,
        'edities': edities,
        # 'tileserver': os.environ.get("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png")
        'tileserver': os.environ.get("TILESERVER")
    }
    return render( request,'index.html',context)

def search_deelnemers(request):
    if request.method == "POST":
        searched = request.POST['searched']
        if 'edition' not in request.session:
            request.session['edition'] = ""
        edition = request.session["edition"]
        deelnemers = DatacollectorPerson.objects.filter(first_name__icontains=searched)
        return render(request, 'search_deelnemers.html',{'searched':searched,
        'deelnemers': deelnemers, 'tileserver': os.environ.get("TILESERVER")})
    else:
        return render(request)


    

def show_deelnemer(request, person_id):
    with open('hagelandse101/static/route.json', 'r', encoding='utf_8') as f:
        routejson = json.load(f)
    if 'personen' not in request.session:
        request.session['personen'] = []
    personenlijst = request.session['personen']
    if person_id not in personenlijst:
        personenlijst.append(person_id)
    request.session['personen'] = personenlijst
    personen = DatacollectorPerson.objects.filter(pk__in=personenlijst)
    
    return render(request, 'show_deelnemers.html', {'personen':personen, 'personenlijst': personenlijst,'tileserver': os.environ.get("TILESERVER")})

def show_deelnemers(request):
    with open('hagelandse101/static/route.json', 'r', encoding='utf_8') as f:
        routejson = json.load(f)
    if 'personen' not in request.session:
        request.session['personen'] = []
    personenlijst = request.session['personen']
    personen = DatacollectorPerson.objects.filter(pk__in=personenlijst)

    tileserver = os.environ.get("TILESERVER")
    return render(request, 'show_deelnemers.html', {'personen':personen, 'personenlijst': personenlijst,'tileserver': tileserver})

  
def validate_persoon(request):
    person_id = request.GET.get('person_id', None)
    person = DatacollectorPerson.objects.filter(id=person_id).first()
    participation = DatacollectorParticipation.objects.get(person_id=person_id)
    positie = DatacollectorPosition.objects.filter(participation_id=participation.id).last()
    ser_person = serializers.serialize('json', [ person, ])
    data = {
        'person': ser_person,
        'positie': [positie.latitude, positie.longitude],
        'distance': positie.distance
    }
    
    return JsonResponse(data)

def delete_persoon(request):
    person_id = int(request.GET.get('person_id', None))
    personenlijst = request.session['personen']
    personenlijst.pop(person_id)
    

def track(request):
    
    personenlijst = request.session['personen']
    
    personen = DatacollectorPerson.objects.filter(pk__in=personenlijst)
    
    deelnames = DatacollectorParticipation.objects.filter(person_id__in=personenlijst)
    ser_personen = serializers.serialize('json', personen.all())
    

    posities = []
    for deelname in deelnames:
        positie = DatacollectorPosition.objects.filter(participation_id=deelname.id).last()
        if positie is not None:
            posities.append([positie.latitude, positie.longitude, positie.distance])
        
    data = {
        'personen': ser_personen,
        'posities':posities,
       
    }
    return JsonResponse(data)

def show_controlpoints(request):
    with open('hagelandse101/static/route.json', 'r', encoding='utf_8') as f:
        routejson = json.load(f)
    
    return render(request,'show_controlpoints.html', {'routejson': routejson, 'tileserver': os.environ.get("TILESERVER")})




