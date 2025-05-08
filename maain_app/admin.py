from django.contrib import admin

from maain_app.models import Customer
admin.site.site_title="kanyi.com"
admin.site.site_header="sacco application"

# Register your models here.

class CustomerUserAdmin(admin.ModelAdmin):
    list_display = ['names', 'email', 'gender', ]
    list_per_page = 20
    search_fields = ['name','email','dob','phone']
    list_filter = ['gender']




admin.site.register(Customer,CustomerUserAdmin)
