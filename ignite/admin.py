__author__ = 'hongleviet'
from django.contrib import admin
from ignite.models import *

class CompanyAdmin(admin.ModelAdmin):
    #filter_horizontal = ('founders',)
    raw_id_fields = ('founders',)

admin.site.register(Company, CompanyAdmin)
admin.site.register(Person)
admin.site.register(TeamMember)
admin.site.register(Founder)
admin.site.register(Category)


