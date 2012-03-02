from django.conf.urls.defaults import *
from django.views.generic import ListView
from .models import Status
from .settings import SITE_TITLE

urlpatterns = patterns('sitestatus_nonrel.views',
    url('^$',
        ListView.as_view(
            queryset=Status.objects.all().order_by('link_text'),
            context_object_name='statuses',
            template_name='index.html')),
            extra_content=dict(sitetitle=SITE_TITLE),
    url('^update/$', 'update')
)
