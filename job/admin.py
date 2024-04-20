from django.contrib import admin
from .models import Job,Category,ApplyJob
# Register your models here.
@admin.register(Job)
class JObAdmin(admin.ModelAdmin):
    list_display = 'id' , 'job_name'
    list_display_links = 'job_name',

admin.site.register(Category)
admin.site.register(ApplyJob)

