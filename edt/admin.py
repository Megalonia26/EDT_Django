from django.contrib import admin

from .models import Day, Hour, To, Professor, Subject, Classroom, Edt

admin.site.register(Day)
admin.site.register(Hour)
admin.site.register(To)
admin.site.register(Professor)
admin.site.register(Subject)
admin.site.register(Classroom)

class EdtAdmin(admin.ModelAdmin):
    ordering = ["hour__hour"]


admin.site.register(Edt, EdtAdmin)