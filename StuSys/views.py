from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext


@login_required
def Index(request):
    kwvars = {}
    return render_to_response('index.html',kwvars,RequestContext(request))