from django.contrib import admin
from hagelandse101 import models
from django import forms


admin.site.register(models.DatacollectorPerson)
admin.site.register(models.DatacollectorParticipation)
admin.site.register(models.DatacollectorEdition)


class JsonImportForm(forms.Form):
    json_upload = forms.FileField()

