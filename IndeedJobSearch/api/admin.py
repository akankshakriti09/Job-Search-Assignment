from django.contrib import admin
from .models import Job

# Register your models here.
@admin.register(Job)
class ProfileModelAdmin(admin.ModelAdmin):
    list_display = ['title','company_name','company_location','salary']
    list_editable = ['company_name','company_location','salary']