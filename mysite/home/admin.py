
from django.contrib import admin
from home.models import Contact


# Register your models here.

admin.site.register(Contact)

#for changing administration title

admin.site.site_header = "N techWelly Admin"
admin.site.site_title = "N techWelly Admin Portal"
admin.site.index_title = "Welcome to N techWelly Researcher Portal"
