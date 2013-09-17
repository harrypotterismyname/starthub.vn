# Create your views here.
from django.db.models import Q
from django.core.paginator import Paginator
from django.shortcuts import  render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from ignite.forms import AddCompanyForm

from ignite.models import *
from itertools import chain
import operator

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


def go_home(request):
    return  HttpResponseRedirect("/")

def home(request):

    try:
        aboutus_homepage = Meta_info.objects.get( slug = "aboutus_homepage")
        head_description =  Meta_info.objects.get( slug = "head_description")
    except:
        aboutus_homepage = None
        head_description = None

    page = request.GET.get("page",1)
    page_size = 30
    max_items = 0

    # categories = Category.objects.all()
    categories = Category.objects.order_by('name').all()


    search_query = request.GET.get('q', None)


     #TODO: implement search function
    if search_query:
        search_query =  search_query.lower()
        # | Q(name_en__contains = search_query)  | Q(name_vi__contains = search_query)
        companies = Company.objects.filter(name__icontains = search_query).exclude(is_private = True).order_by("-id")#[(page-1)*page_size:page*page_size ]

    else:


        companies = Company.objects.all().exclude(is_private = True).order_by("-id")#[(page-1)*page_size:page*page_size ]
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
            'categories': categories,
            'aboutus_homepage': aboutus_homepage,
            'head_description': head_description,

            })


    return render_to_response('index.html', variables )


def category(request, categories):



    page = request.GET.get("page",1)
    page_size = 30
    #max_items = 0

    categories = categories.lower()

    cbcategories = Category.objects.order_by('name').all()

    cats = categories.split(',')
    companies = []
    for cat in cats:
        category = Category.objects.get(slug = cat)
        new_list = list(category.cat_list.all())
        new_list += list(Company.objects.filter( category_id = category.id ).exclude(is_private = True).order_by("-id"))#[(page-1)*page_size:page*page_size ]

        #max_items +22=  Company.objects.filter( category_id = category.id ).count()

        companies += new_list

    companies = list(set(companies))

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
            'category': category,
            'categories': cbcategories
            })


    return render_to_response('index.html', variables )


def company(request, id):


    company = get_object_or_404(Company, pk=id)
    if company.is_private:
        return HttpResponseRedirect('/')

    team = company.teammember_set.all()
    founders = company.founders.all()


    member_list = list(chain(founders,team))
    say_thanks = False
    categories = Category.objects.order_by('name').all()

    if request.method == "POST":

        suggestion = Suggestion( content = request.POST.get('content', ''), email = request.POST.get('email','') )
        suggestion.company = company
        suggestion.save()

        say_thanks = True






    variables = RequestContext(request, {
           'company': company,
           'team': member_list,
           'say_thanks': say_thanks,
            'categories': categories

            })


    return render_to_response('company.html', variables )


def thanks(request):

    variables = RequestContext(request, {


            })


    return render_to_response('thanks.html', variables )

def about_us(request):

    #company = get_object_or_404(Company, pk=id)
    try:
        full_aboutus = Meta_info.objects.get(slug = "full_aboutus")
    except:
        full_aboutus = ""

    variables = RequestContext(request, {

               'full_aboutus': full_aboutus,
            })




    return render_to_response('aboutus.html', variables )

def add_your_company(request):

    if request.method == 'POST': # If the form has been submitted...
        form = AddCompanyForm(request.POST, request.FILES) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            ins = form.save()

            logo =  request.FILES.get('logo',None)
            if (logo):
                ins.logo = logo
            ins.is_private = True
            ins.save()
            # Process the data in form.cleaned_data
            # ...
            return HttpResponseRedirect('/thanks/') # Redirect after POST
    else:
        form = AddCompanyForm() # An unbound form



    variables = RequestContext(request, {

               'form': form,
            })


    return render_to_response('add_your_company.html', variables )