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

    url(r'^home/&', views.home, name='reports/home'),
    url(r'alunos/telefones', views.alunos_telefones, name='reports/alunos'),
    url(r'alunos/portaria', views.alunos_portaria, name='reports/portaria'),
    url(r'alunos/presenca', views.alunos_presenca, name='reports/presenca'),
    url(r'voluntarios/portaria', views.voluntarios_portaria, name='reports/presenca'),
    # url(r'redacao', views.redacao, name='redacao'),
    # url(r'^alunos/login/$', views.redirect_to_home, name='redirect_to_home'),
    url(r'$^', views.home, name='reports/home'),

]

