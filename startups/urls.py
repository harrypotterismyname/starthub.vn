from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from ignite.api import *
from tastypie.api import Api


#company_resource = CompanyResource()
#user_resource = UserResource()

v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(CompanyResource())

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from ignite.views import *

urlpatterns = patterns('',
    # Examples:
     url(r'^$', home, name='home'),
     url(r'^company/(?P<id>\d+)-(.+)/', company),
     url(r'^category/$', go_home),
     url(r'^category/(?P<categories>.+)/$', category),
     url(r'^category/(?P<categories>.+)$', category),
     url(r'^about-us/$', about_us ),
      url(r'^add-your-company/$', add_your_company),
      url(r'^thanks/$', thanks),
     url(r'^events/$', events),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),

      (r'^inplaceeditform/', include('inplaceeditform.urls')),
      (r'^accounts/profile/', RedirectView.as_view(url = '/')),



      (r'^accounts/', include('registration.backends.default.urls')),
          (r'^i18n/', include('django.conf.urls.i18n')),
         (r'^tinymce/', include('tinymce.urls')),


          (r'^api/', include(v1_api.urls)),


)
