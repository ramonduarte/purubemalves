from django.conf.urls import include, url
from django.contrib import admin
import home.views

admin.autodiscover()  # DON'T TOUCH THIS LINE


urlpatterns = [
    # Examples:
    # url(r'^$', 'transparency.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
]