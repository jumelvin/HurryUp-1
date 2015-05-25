from django import forms

class ContactForm(forms.Form):
    sujet = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    envoyeur = forms.EmailField(label="Votre adresse mail")
    renvoi = forms.BooleanField(help_text="Cochez si vous souhaitez obtenir une copie du mail envoye.", required=False)

class TrajetsForm(forms.Form):
    Depart = forms.CharField(max_length=200)
    Arrivee = forms.CharField(max_length=200)
