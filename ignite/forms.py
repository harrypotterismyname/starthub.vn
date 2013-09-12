

from django import forms
from django.forms import ModelForm
from ignite.models import Company

class AddCompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'one_sentence_description', 'description', 'phone', 'email','address', 'website', 'founding_year', 'category', 'logo']
