from django.conf.urls import patterns, url
from journal.views import UpdateCompletedItemView, ChangeIndicatorForItemView
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('produccion.views',

    url(r'^item/completed/(?P<pk>\d+)/$', login_required(UpdateCompletedItemView.as_view()), name='update_completed_item'),
    url(r'^item/indicator/(?P<pk>\d+)/$', login_required(ChangeIndicatorForItemView.as_view()), name='update_indicator_item'),

)