from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from ignite.views import *

urlpatterns = patterns('',
    # Examples:
     url(r'^$', home, name='home'),
     url(r'^company/(?P<id>\d+)-(.+)/', company),
     url(r'^category/(?P<categories>.+)/', category),
     url(r'^about-us/$', about_us),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),

      (r'^inplaceeditform/', include('inplaceeditform.urls')),
      (r'^accounts/profile/', RedirectView.as_view(url = '/')),



      (r'^accounts/', include('registration.backends.default.urls')),
)
