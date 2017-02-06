from django.conf.urls import include, url
from django.contrib import admin
import website.views


admin.autodiscover()  # DON'T TOUCH THIS LINE


urlpatterns = [
    # Examples:
    # url(r'^$', 'transparency.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^updatedb', website.views.updatedb, name='updatedb'),
    url(r'^updatenewdb', website.views.updatenewdb, name='updatenewdb'),
]
