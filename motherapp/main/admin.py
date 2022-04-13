from django.contrib import admin
from .models import Participant

# Register your models here.
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('identity', 'Full_Name', 'Email', 'Phone_No', 'Created_on', 'Available', 'Status')
    list_editable = ('Status', 'Available')
    prepopulated_fields = {'identity' : ('Phone_No', 'Full_Name')}
admin.site.register(Participant, ParticipantAdmin)