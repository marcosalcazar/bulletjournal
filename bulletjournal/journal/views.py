from collections import OrderedDict
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from journal.models import Event, Task, Item, CompletableItem
import calendar
import datetime
import json
from django.views.generic.edit import UpdateView, BaseUpdateView
from django.shortcuts import render_to_response
from django.utils import simplejson



class JSONResponseMixin(object):
    """
    A mixin that can be used to render a JSON response.
    """
    def render_to_json_response(self, context, **response_kwargs):
        """
        Returns a JSON response, transforming 'context' to make the payload.
        """
        return HttpResponse(
            self.convert_context_to_json(context),
            content_type='application/json',
            **response_kwargs
        )

    def convert_context_to_json(self, context):
        "Convert the context dictionary into a JSON object"
        # Note: This is *EXTREMELY* naive; in reality, you'll need
        # to do much more complex handling to ensure that arbitrary
        # objects -- such as Django model instances or querysets
        # -- can be serialized as JSON.
        return json.dumps(context)


class MonthView(TemplateView):
    
    template_name = 'journal/monthview.html'
    
    def get_context_data(self, **kwargs):
        c = TemplateView.get_context_data(self, **kwargs)
        today = datetime.date.today()
        c['today'] = today
        c['tasks'] = Task.objects.filter(date__month=today.month,
                                         user=self.request.user,
                                         father__isnull=True)
        c['events'] = OrderedDict()
        events = Event.objects.filter(date__month=today.month,
                                      user=self.request.user)
        (_, last_day) = calendar.monthrange(today.year, today.month)
        for i in range(0, last_day):
            c['events'][datetime.date(today.year, today.month, i + 1)] = []
        for event in events:
            c['events'][event.date].append(event)
        print c['events']
        return c


class UpdateCompletedItemView(JSONResponseMixin, BaseUpdateView):
    model = CompletableItem
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        
        completed = simplejson.loads(request.POST.get('completed'))
        self.object.completed = completed
        self.object.save()
        
        return self.render_to_json_response({
            'cod':1,
            'msg':'Ok'
        })

        
        