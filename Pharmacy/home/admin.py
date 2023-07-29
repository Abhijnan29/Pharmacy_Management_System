from django.contrib import admin
from home.models import contact
from home.models import Med_Prod
from home.models import order

# Register your models here.
admin.site.register(contact)
admin.site.register(Med_Prod)
admin.site.register(order)