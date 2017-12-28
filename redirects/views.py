from django.http import HttpResponse, HttpResponseRedirect

from django.shortcuts import get_object_or_404, render
from .models import Tracking


def index(request):
    return HttpResponse("")

def redirect(request, tracking_text):
    t = get_object_or_404(Tracking, tracking_text=tracking_text)
    return HttpResponseRedirect(t.tracking_link)
