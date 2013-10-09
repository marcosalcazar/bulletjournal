from bulletjournal.views import JSONResponseMixin
from collections import OrderedDict
from django.utils import simplejson
from django.views.generic.base import TemplateView
from django.views.generic.edit import BaseUpdateView
from journal.models import Event, Task, CompletableItem, Item, Note
import calendar
import datetime
from django.db.models import Q
from itertools import chain


class MonthView(TemplateView):
    
    template_name = 'journal/monthview.html'
    
    def get_context_data(self, **kwargs):
        c = TemplateView.get_context_data(self, **kwargs)
        
        today = datetime.date.today()
        c['today'] = today # Added to the context so we can use it in the template
        
        # Query all tasks for the user, only parents, for this month
        c['tasks'] = Task.objects.filter(date__month=today.month,
                                         user=self.request.user,
                                         father__isnull=True)
        
        # Query all events for the user, for this month
        events = Event.objects.filter(date__month=today.month,
                                      user=self.request.user)
        
        # I need to put them under the correct day, so I create an ordered dict, using
        # the days of the month for as keys, and appending the events to the days
        # when the day of the event matches 
        c['events'] = OrderedDict()
        (_, last_day) = calendar.monthrange(today.year, today.month) # First argument discouraged
        
        # Initialize the OrderedDict
        for i in range(0, last_day):
            c['events'][datetime.date(today.year, today.month, i + 1)] = []
        
        # Fill the dict with events
        for event in events:
            c['events'][event.date].append(event)
        
        # returning the context
        return c


class DailyCalendar(TemplateView):
    
    template_name = 'journal/dailycalendar.html'
    
    def get_context_data(self, **kwargs):
        c = TemplateView.get_context_data(self, **kwargs)
        
        today = datetime.date.today()
        c['today'] = today # Added to the context so we can use it in the template
        
        days = OrderedDict()
        c['days'] = days
        
        q = Q(date=today) & Q(user=self.request.user)
        tasks = Task.objects.filter(q).filter(father__isnull=True).all()
        events = Event.objects.filter(q).all()
        notes = Note.objects.filter(q).all()
        
        days[today] = chain(tasks, events, notes) 
        
        print c['days']
        
        return c


class UpdateCompletedItemView(JSONResponseMixin, BaseUpdateView):
    model = CompletableItem

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        completed = simplejson.loads(request.POST.get('completed'))
        self.object.completed = completed
        self.object.save()

        return self.render_to_json_response({
            'cod': 1,
            'msg': 'Item updated'
        })


class ChangeIndicatorForItemView(JSONResponseMixin, BaseUpdateView):
    model = Item

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        indicator = request.POST.get('indicator')
        self.object.indicator = indicator
        self.object.save()

        return self.render_to_json_response({
            'cod': 1,
            'msg': 'Item Updated'
        })
