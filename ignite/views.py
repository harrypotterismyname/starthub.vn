# Create your views here.

from django.core.paginator import Paginator
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



    page = request.GET.get("page",1)
    page_size = 10
    max_items = 0


    search_query = request.GET.get('q', None)

     #TODO: implement search function
    if search_query:
       
        companies = Company.objects.filter( name__contains = search_query ).order_by("-id")#[(page-1)*page_size:page*page_size ]

    else:


        companies = Company.objects.all().order_by("-id")#[(page-1)*page_size:page*page_size ]
        #max_items +=  Company.objects.all().count()

    # max_page = max_items/page_size
    # if max_items%page_size > 0:
    #     max_page += 1

    p = Paginator(companies, page_size)

    current_page = p.page(page)
    company_list = current_page.object_list


    listA, listB = seperate_list(company_list)

    variables = RequestContext(request, {
            'companies': companies,
            'listA': listA,
            'listB': listB,
            'page':page,
            'paging': p,
            'current_page': current_page,

            })


    return render_to_response('index.html', variables )



def category(request, categories):



    page = request.GET.get("page",1)
    page_size = 10
    #max_items = 0

    cats = categories.split(',')
    companies = []
    for cat in cats:
        category = Category.objects.get(slug = cat)

        new_list = Company.objects.filter( category_id = category.id ).order_by("-id")#[(page-1)*page_size:page*page_size ]
        #max_items +=  Company.objects.filter( category_id = category.id ).count()

        companies += new_list

    p = Paginator(companies, page_size)

    current_page = p.page(page)
    company_list = current_page.object_list




    listA, listB = seperate_list(company_list)

    variables = RequestContext(request, {
            #'companies': companies,
            'listA': listA,
            'listB': listB,
             'page':page,
            'paging': p,
            'current_page': current_page,
            'category': category

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



def about_us(request):

    variables = RequestContext(request, {


            })


    return render_to_response('aboutus.html', variables )