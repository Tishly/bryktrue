from django.contrib import admin
from .models import Jobs_Listings, JobPosting

# Register your models here.
admin.site.register(Jobs_Listings)
admin.site.register(JobPosting)