from django.conf.urls import patterns, url
from journal.views import UpdateCompletedItemView, ChangeIndicatorForItemView,\
    MonthView, DailyCalendar
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('journal.views',

    url(r'^month_view/$', login_required(MonthView.as_view()), name='month_view'),
    url(r'^daily_calendar/$', login_required(DailyCalendar.as_view()), name='daily_calendar'),
    

    url(r'^item/completed/(?P<pk>\d+)/$', login_required(UpdateCompletedItemView.as_view()), name='update_completed_item'),
    url(r'^item/indicator/(?P<pk>\d+)/$', login_required(ChangeIndicatorForItemView.as_view()), name='update_indicator_item'),

)