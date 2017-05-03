from django.conf.urls import include, url
from django.contrib import admin
from website import views


admin.autodiscover()  # DON'T TOUCH THIS LINE


urlpatterns = [
# Autocomplete views
url(
    r'^curso-autocomplete/$',
    views.CursoAutocomplete.as_view(create_field='nome'),
    name='curso-autocomplete',
),
# url(r'^equipe-autocomplete/$', website.views.wm.EquipeAutocomplete.as_view(), name='equipe-autocomplete'),
# url(r'^autor-autocomplete/$', website.views.wm.AutorAutocomplete.as_view(), name='autor-autocomplete'),

]



