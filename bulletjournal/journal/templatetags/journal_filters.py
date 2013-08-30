from django import template
from journal.models import Task, Event, Note
from django.template import loader, Context

register = template.Library()


@register.simple_tag(takes_context=True)
def render_item(context, item):
    choices = {
        Task: 'journal/_task.html',
        Event: 'journal/_event.html',
        Note: 'journal/_event.html'
    }
    t = loader.get_template(choices[type(item)])
    return t.render(Context({
        'item': item
    }))
