from django.conf.urls import patterns, url
from journal.views import UpdateCompletedItemView
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('produccion.views',

    url(r'^item/completed/(?P<pk>\d+)/$', login_required(UpdateCompletedItemView.as_view()), name='update_completed_item'),

)