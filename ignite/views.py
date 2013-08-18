# Create your views here.
from django.shortcuts import  render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404


from ignite.models import *
from itertools import chain
def seperate_list(companies):

    counter = len(companies)

    half_list = counter/2

    if counter%2 == 1:
        half_list += 1

    listA = []
    listB = []

    for i in range(0,counter):
        if i <= (half_list-1):
            listA.append(companies[i])
        else:
            listB.append(companies[i])

    return listA, listB

def home(request):

    companies = Company.objects.all().order_by("?")

    listA, listB = seperate_list(companies)

    variables = RequestContext(request, {
            'companies': companies,
            'listA': listA,
            'listB': listB,

            })


    return render_to_response('index.html', variables )


def company(request, id):
    company = get_object_or_404(Company, pk=id)

    team = company.teammember_set.all()
    founders = company.founders.all()


    member_list = list(chain(founders,team))




    variables = RequestContext(request, {
           'company': company,
           'team': member_list

            })


    return render_to_response('company.html', variables )