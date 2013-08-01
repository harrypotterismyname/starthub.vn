# Create your views here.
from django.shortcuts import  render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect
def home(request):

     variables = RequestContext(request, {
            'data': "Hello, I'm here",

            })


     return render_to_response('index.html', variables )