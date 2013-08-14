# Create your views here.
from django.shortcuts import  render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404


from ignite.models import *

def home(request):

    companies = Company.objects.all()

    variables = RequestContext(request, {
            'companies': companies,

            })


    return render_to_response('index.html', variables )


def company(request, id):
    company = get_object_or_404(Company, pk=id)

    variables = RequestContext(request, {
           'company': company

            })


    return render_to_response('company.html', variables )