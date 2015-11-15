from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

from moolah import routes


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include(routes.urlpatterns)),
    url(r'^api/reports/', include('reporting.urls', namespace='reports')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^$', login_required(TemplateView.as_view(template_name='index.html')))
]


if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    from django.conf.urls.static import static

    urlpatterns += staticfiles_urlpatterns()
