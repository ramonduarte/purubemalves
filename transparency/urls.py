from django.conf import settings
from django.conf.urls import include, url, static
from django.contrib import admin
import controle_de_frequencia
import website.views
import home.views
import issues.views


admin.autodiscover()  # DON'T TOUCH THIS LINE


urlpatterns = [
    # Examples:
    # url(r'^$', 'transparency.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # url(r'^updatedb', website.views.updatedb, name='updatedb'),
    # url(r'^updatenewdb', website.views.updatenewdb, name='updatenewdb'),
    url(r'^getcep', website.views.getcep, name='getcep'),

    # url(r'^$', include('home.urls')),
    url(r'^index$', home.views.index, name='home'),
    url(r'contato$', home.views.contato, name='contato'),
    url(r'^equipe$', home.views.equipe, name='equipe'),
    # url(r'^estude$', home.views.estude, name='estude'),
    url(r'^curso$', home.views.curso, name='curso'),
    url(r'^resultados$', home.views.resultados, name='resultados'),
    url(r'$^', home.views.index, name='home'),

    url(r'^frequencia/', include('controle_de_frequencia.urls')),

    url(r'^isencao/', include('politicas_afirmativas.urls')),

    url(r'^redacao/', include('projeto_redacao.urls')),

    url(r'^alunos/', include('alunos.urls')),

    url(r'^protocolo$', issues.views.protocolo, name='protocolo'),
] + static.static(settings.ENCRYPT_URL, document_root=settings.ENCRYPT_ROOT)
