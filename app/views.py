from django.shortcuts import render
from django.db.models.functions import Length

# Create your views here.
from app.models import *
def display_topic(request):
    qst=Topic.objects.all()
    d={'topics':qst}
    return render (request,'display_topic.html',d)

def display_webpage(request):
    qsw=Webpage.objects.all()
    qsw=Webpage.objects.filter(topic_name='cricket')
    qsw=Webpage.objects.exclude(topic_name='cricket')
    qsw=Webpage.objects.all()[:3]
    qsw=Webpage.objects.order_by('name')
    qsw=Webpage.objects.order_by('-name')
    qsw=Webpage.objects.order_by(Length('name'))
    qsw=Webpage.objects.filter(topic_name='cricket').order_by('-name')
    qsw=Webpage.objects.all()
    d={'webpage':qsw}
    return render (request,'display_webpage.html',d)

def display_access(request):
    qsa=AccessRecord.objects.all()
    qsa=AccessRecord.objects.all().order_by('date')
    qsa=AccessRecord.objects.order_by(Length('name'))

    d={'access':qsa}
    return render(request,'display_access.html',d)
