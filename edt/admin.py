from django.contrib import admin

from .models import Day, Hour, To, Professor, Subject, Classroom, ProfessorAvailability

admin.site.register(Day)
admin.site.register(Hour)
admin.site.register(To)
admin.site.register(Professor)
admin.site.register(Subject)
admin.site.register(Classroom)
admin.site.register(ProfessorAvailability)