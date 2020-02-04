from django.contrib import admin
from .models import Property, PropertyType, PropertyImages, RealEstateAgency, Agent


# Register your models here.
admin.site.register(Property)
admin.site.register(PropertyType)
admin.site.register(PropertyImages)
admin.site.register(RealEstateAgency)
admin.site.register(Agent)

