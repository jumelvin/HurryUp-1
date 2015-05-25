from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Hurry_Up__.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'signups.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hurry/', include('hurry.urls')),
    url(r'^trajets/$', 'hurry.views.trajets', name='trajets'),
    url(r'^confirmation/$', 'signups.views.confirmation', name='confirmation'),
    url(r'^cover/$', 'signups.views.cover', name='cover'),
    url(r'^register/$', 'signups.views.register', name='register'),
    url(r'^reveil/$', 'signups.views.reveil', name='reveil'),
    url(r'^geodjango/$', 'signups.views.geodjango', name='geodjango'),
    url(r'^accounts/', include('registration.backends.default.urls')),

)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                             document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                             document_root=settings.MEDIA_ROOT)