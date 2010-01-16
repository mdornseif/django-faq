from django.conf.urls.defaults import *
from faq.views import faq_list_by_group, submit_faq

urlpatterns = patterns('',

url (
    r'^$',
    faq_list_by_group,
    name = 'faq',
    ),
url (
    r'^submit_faq/$',
    submit_faq,
    {'success_url': '/faq/'},
    name = 'submit',
    ),
)

