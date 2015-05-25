# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from hurry.forms import ContactForm
from hurry.forms import TrajetsForm

def base(request):
    return render(request, 'base.html', locals())
# Create your views here.


def contact(request):
    if request.method == 'POST':
        """s'il s'agit d'une requete POST"""
        form = ContactForm(request.POST)
        """ Nous reprenons les donnees"""

        if form.is_valid(): # Nous vérifions que les données envoyées sont valides

            # Ici nous pouvons traiter les données du formulaire
            sujet = form.cleaned_data['sujet']
            message = form.cleaned_data['message']
            envoyeur = form.cleaned_data['envoyeur']
            renvoi = form.cleaned_data['renvoi']

            # Nous pourrions ici envoyer l'e-mail grâce aux données que nous venons de récupérer

            envoi = True

    else: # Si ce n'est pas du POST, c'est probablement une requête GET
        form = ContactForm()  # Nous créons un formulaire vide

    return render(request, 'contact.html', locals())

def trajets(request):
    if request.method == 'POST':
        """s'il s'agit d'une requete POST"""
        form = TrajetsForm(request.POST)
        """ Nous reprenons les donnees"""

        if form.is_valid(): # Nous vérifions que les données envoyées sont valides

            # Ici nous pouvons traiter les données du formulaire
            Depart = form.cleaned_data['Depart']
            Arrivee = form.cleaned_data['Arrivee']

    else: # Si ce n'est pas du POST, c'est probablement une requête GET
        form = TrajetsForm()  # Nous créons un formulaire vide

    return render(request, 'trajets.html', locals())
