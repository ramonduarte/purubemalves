from django.conf.urls import url, include
from django.contrib import admin
from reports import views
from django.contrib.auth import views as auth_views


admin.autodiscover()  # DON'T TOUCH THIS LINE

urlpatterns = [
    # django.auth views
    url(r'^login/$', auth_views.login, {
        'template_name': 'alunos/login.html',
    }, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^admin/', admin.site.urls),

    # Social OAuth logins
    url(r'^oauth/', include('social_django.urls', namespace='social')),

    # Reports views
    #
    # Main view
    url(r'^home/&', views.home, name='reports/home'),
    #
    # Alunos views
    url(r'alunos/telefones', views.alunos_telefones, name='reports/alunos/telefones'),
    url(r'alunos/portaria', views.alunos_portaria, name='reports/alunos/portaria'),
    url(r'alunos/presenca', views.alunos_presenca, name='reports/alunos/presenca'),
    #
    # Voluntarios views
    url(r'voluntarios/portaria', views.voluntarios_portaria, name='reports/voluntarios/portaria'),
    url(r'voluntarios/contatos', views.voluntarios_contatos, name='reports/voluntarios/contatos'),
    #
    # Simulados views
    url(r'simulados/equerj/cartao', views.simulados_equerj_cartao, name='reports/simulados/equerj/cartao'),
    url(r'simulados/equerj/ata', views.simulados_equerj_ata, name='reports/simulados/equerj/ata'),

    # Catch-all
    url(r'$^', views.home, name='reports/home'),

]

