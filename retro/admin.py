from django.contrib import admin

from .models import *

# Register your models here.

admin.site.site_header = 'Retro Tool Administration'
admin.site.site_title = 'Retro Tool Administration'
admin.site.register(Project)
admin.site.register(Team)
admin.site.register(Sprint)
admin.site.register(Owner)
admin.site.register(Status)
admin.site.register(Feedback)
