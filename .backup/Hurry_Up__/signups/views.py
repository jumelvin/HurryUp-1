#python first
#django second
#apps
#local directory
# -*- coding: utf-8 -*-

from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect

# Create your views here.
from .forms import SignUpForm

def home(request):

    form = SignUpForm(request.POST or None)
    
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
        #send_mail(subject, message, from_email, to_list, fail_silently=True)
        subject = 'Merci de votre inscription sur HurryUp!'
        message = 'Bienvenue sur HurryUp! Vous pouvez des maintenant profiter de l experience HurryUp!\nPour toute information complementaire, veuillez vous reporter aux tutoriels presents sur le site.\n A bientot.\n L equipe HurryUp!\nhttp://jxodj8p2.apps.lair.io/'
        from_email = settings.EMAIL_HOST_USER
        to_list = [save_it.email]
        send_mail(subject,message,from_email,to_list,fail_silently=True)
        messages.success(request, 'Vous allez recevoir un mail de confirmation .')
        return HttpResponseRedirect('/confirmation/')

    return render_to_response("signup.html",
                              locals(),
                              context_instance=RequestContext(request))


def confirmation(request):

    return render_to_response("confirmation.html",
                              locals(),
                              context_instance=RequestContext(request))

def cover(request):

    return render_to_response("cover.html",
                              locals(),
                              context_instance=RequestContext(request))

def register(request):

    return render_to_response("register.html",
                              locals(),
                              context_instance=RequestContext(request))
                              
def reveil(request):

    return render_to_response("reveil.html",
                              locals(),
                              context_instance=RequestContext(request))

def custom_login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("geodjango.html")
    else:
        return render_to_response('404.html', {},
                                  context_instance=RequestContext(request))

def geodjango(request):

    return render_to_response("geodjango.html",
                              locals(),
                              context_instance=RequestContext(request))

def handler404(request):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request):
    response = render_to_response('500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response


