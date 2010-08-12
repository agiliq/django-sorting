from django.shortcuts import render_to_response
from django.template import RequestContext
from sortingtestapp.models import SortableThingy, SortableThingy2

def index(request):    
    s1 = SortableThingy.objects.all()
    return render_to_response("sortingtestapp/index.html", locals(), RequestContext(request))


def index2(request):    
    s2 = SortableThingy2.objects.all()
    return render_to_response("sortingtestapp/index2.html", locals(), RequestContext(request))
