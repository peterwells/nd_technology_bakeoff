from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'oracle_test.views.academic_terms'),
)