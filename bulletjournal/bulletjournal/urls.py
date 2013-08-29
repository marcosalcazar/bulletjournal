from django.conf.urls import patterns, include, url
from journal.views import MonthView
from django.contrib.auth.decorators import login_required


urlpatterns = patterns('',

    url(r'^$', login_required(MonthView.as_view()), name='home'),
    url(r'^journal/', include('journal.urls', namespace='journal')),
    
    url(r'^accounts/login/$', 'django.contrib.auth.views.login',
        {'template_name': 'login.html'}, name='login'),

    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout',
        {'template_name': 'logout.html'}, name='logout')

)
