from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import TemplateView


class DashboardView(TemplateView):
    template_name = 'website/calendar.html'


def get_data(request):
    data = [
        dict(title='Lunch', start='2018-10-22 10:00', end='2018-10-22 10:30', allDay=False, className='event-azure'),
        dict(title='Lunch', start='2018-10-23 11:00', end='2018-10-22 11:30', allDay=False, className='event-orange'),
        dict(title='Lunch', start='2018-10-24 12:00', end='2018-10-22 12:30', allDay=False, className='event-green'),
        dict(title='Lunch', start='2018-10-25 13:00', end='2018-10-22 13:30', allDay=False, className='event-red'),
        dict(title='Lunch', start='2018-10-26 14:00', end='2018-10-22 14:30', allDay=False, className='event-blue')
    ]
    return JsonResponse(data, safe=False)
