from django.contrib import admin
from .models import ServiceTrackRequests, CustomerProfile

# Register your models here.

admin.site.register(ServiceTrackRequests)
admin.site.register(CustomerProfile)