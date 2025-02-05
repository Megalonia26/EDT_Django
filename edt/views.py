from django.shortcuts import render

from .models import Edt

def index(request):

    timetable = Edt.objects.all()

    context = {
        'timetable': timetable
    }

    return render(request, 'edt/index.html', context)