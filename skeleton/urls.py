from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from registration.backends.simple.views import RegistrationView

# Create a new class that redirects the user to the home page, if successful at logging
class MyRegistrationView(RegistrationView):
    def get_success_url(self, request, user):
        return '/home/'

urlpatterns = patterns('',
    url(r'^$', 'skeleton.views.home', name='home'),

    url(r'^about/$', 'skeleton.views.about', name='about'),

    url(r'^accounts/profile/$', 'skeleton.views.user_profile', name='user_profile'),
    url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
    (r'^accounts/', include('registration.backends.simple.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/$', 'skeleton.views.home', name='home'),
    url(r'^main/$', include('main.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )

if not settings.DEBUG:
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)