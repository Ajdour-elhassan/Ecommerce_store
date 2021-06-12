from django.shortcuts import render , get_object_or_404
from .models import Services , Works , Contact , Teams , Feedback


def home(request) :

    services = Services.objects.all()
    works = Works.objects.all()
    teams = Teams.objects.all()
    feedback = Feedback.objects.all()

    context = {
        'services' : services ,
        'works' : works ,
        'teams' : teams,
        'feedback' :  feedback
        
    }

    return render(request, 'index.html' , context)


def contact (request) : 
    return render(request, 'contact.html')

def services(request) :
    services = Services.objects.all()
    return render(request, 'services.html', {'services' : services})

def works(request) :
    works = Works.objects.all()
    return render(request, 'works.html', {'works' :  works })



def about(request) :

    feedback = Feedback.objects.all()
    teams = Teams.objects.all()

    return render(request, 'about.html' , { 'feedback' : feedback , 'teams' : teams   })




