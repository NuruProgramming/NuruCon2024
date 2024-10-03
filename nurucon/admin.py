from django.contrib import admin
from .models import Schedule, Setting, Speaker, Sponsor, Registration, MasterOfConference

admin.site.register(Speaker)
admin.site.register(Setting)
admin.site.register(Schedule)
admin.site.register(Sponsor)
admin.site.register(Registration)
admin.site.register(MasterOfConference)
